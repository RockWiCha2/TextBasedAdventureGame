"""
GUI layer for the text adventure.

- Uses pygame + pygame_gui to render a resizable window with a central UITextBox.
- `gui_print()` auto-scales text to fill the text box WITHOUT overflowing by probing
  pygame_gui directly (binary search on <font pixel_size=...>) and checking whether a
  vertical scrollbar is created (which implies overflow).
- Keep edits minimal: this file owns window creation and the always-present DialogLabel.
"""
# Leave to James


import pygame # type: ignore
import pygame_gui # type: ignore

# === Constants ===
FPS = 60                        # target frames per second for the main loop
BG_COLOUR = (30, 30, 36)        # window background
BORDER_COLOUR = (255, 0, 0)     # devtools rectangle colour
TEXTBOX_RECT = (0, 0, 100, 50)  # default size of centre text box
TEXTBOX_MARGIN_X = 0.15  # 15% margin left/right (textbox width = 70% of window)
TEXTBOX_MARGIN_Y = 0.2   # 20% margin top/bottom (textbox height = 60% of window)
FONT_MIN_PX = 10
FONT_MAX_PX = 120               # upper bound for binary search font size
FONT_STEP = 2                   # step used inside the binary search

# === Module state (globals) ===
windowSurface = None  # primary pygame surface (the window)
manager = None        # pygame_gui UIManager, routes events & draws UI
clock = None          # pygame Clock to cap/update FPS
running = False       # main loop sentinel
windowMinWidth = 640  # do not allow the window to get smaller than this
windowMinHeight = 480 # ...or this
windowSize = None     # cached initial window size
mouse_label = None    # devtools: shows mouse x/y
DialogLabel = None    # central UITextBox used for narrative text
dialog_text_last = ""  # last text we showed; used to restore on resize

def _create_dialog_label(win_size):
    """(Re)create the centred UITextBox sized from the current window size."""
    global DialogLabel, manager
    w, h = win_size

    # compute size from margins
    box_w = int(w * (1 - 2 * TEXTBOX_MARGIN_X))
    box_h = int(h * (1 - 2 * TEXTBOX_MARGIN_Y))

    # IMPORTANT: x=y=0 so with centre anchors this rect is centred
    rect = pygame.Rect(0, 0, box_w, box_h)

    DialogLabel = pygame_gui.elements.UITextBox(
        html_text='',
        relative_rect=rect,
        manager=manager,
        anchors={"centerx": "centerx", "centery": "centery"}
    )

def start():
    """Boot the GUI: create window, UI manager and the centred text box.

    Steps:
    1) Init pygame & clock.
    2) Size the window to 80% of the display (with sane minimums).
    3) Create the window surface and UIManager.
    4) Create the always-present centred `UITextBox` used for narrative text.
    """
    global windowSurface, manager, clock, running, windowSize, DialogLabel

    pygame.init()  # Initialise all pygame modules
    clock = pygame.time.Clock()  # Create a Clock object to manage frame rate

    # Get display information and calculate window size with minimum clamps
    displayInfo = pygame.display.Info()
    width = max(int(displayInfo.current_w * 0.8), windowMinWidth)
    height = max(int(displayInfo.current_h * 0.8), windowMinHeight)
    windowSize = (width, height)

    # Create a resizable window surface and set window caption
    windowSurface = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
    pygame.display.set_caption('Adventure Game')

    # Fill background and flip display once at start
    windowSurface.fill(BG_COLOUR)
    pygame.display.flip()

    # Create UI manager with current window size
    manager = pygame_gui.UIManager(windowSize)

    # Create the centred narrative text box sized relative to window
    _create_dialog_label(windowSize)

    running = True  # Set running flag to True to start event loop


# === Public API ===
def gui_print(text):
    """Set the dialog text and auto-scale to the largest size that fits.

    Implementation details:
    - We let pygame_gui perform the layout, then detect overflow by checking if
      `UITextBox` spawned a vertical scrollbar. If it did, the font is too large.
    - Binary search between `FONT_MIN_PX`..`FONT_MAX_PX` to find the largest size
      that fits, then apply it (with a 1px back-off to avoid flicker on edge cases).
    Why this approach? It avoids second-guessing line wrapping, padding and theme
    """
    global DialogLabel
    if DialogLabel is None:
        return
    if text is None:
        text = ""

    # Remember last plain text so we can restore it after a resize
    global dialog_text_last
    dialog_text_last = text

    # --- Robust fit using pygame_gui itself ---
    # We probe sizes by setting the html, rebuilding, and checking if a vertical scroll bar appears.
    # If a scroll bar exists, the content overflowed the height; if not, it fits.

    def fits_with_pixel_size(px: int) -> bool:
        # Temporarily set content at this size and rebuild
        DialogLabel.html_text = f"<font pixel_size={px}>{text}</font>"
        DialogLabel.rebuild()
        # If pygame_gui created a vertical scroll bar, it's too big
        has_scroll = getattr(DialogLabel, 'scroll_bar', None) is not None
        return not has_scroll

    lo, hi = FONT_MIN_PX, FONT_MAX_PX
    best = lo
    # Binary search for the largest size that does not create a scrollbar
    while lo <= hi:
        mid = (lo + hi) // 2
        if fits_with_pixel_size(mid):
            best = mid
            lo = mid + FONT_STEP  # step by FONT_STEP px to converge a tad quicker
        else:
            hi = mid - FONT_STEP

    # Tiny back-off to avoid edge flicker from rounding/layout
    font_size = max(FONT_MIN_PX, best - 1)

    # Set the font size dynamically using pixel_size
    DialogLabel.html_text = f"<font pixel_size={font_size}>{text}</font>"
    DialogLabel.rebuild()


def pump():
    """Run one frame: process events, update UI, draw.

    Notes on resize: `manager.clear_and_reset()` clears UI state. If your
    `DialogLabel` ever disappears on resize (theme dependent), recreate it here.
    """
    global running, windowSurface, manager

    timeDelta = clock.tick(FPS) / 1000.0  # Limit frame rate to FPS and get elapsed time in seconds

    for event in pygame.event.get():  # Process all events in the event queue
        if event.type == pygame.QUIT:  # Check if the user has requested to close the window
            running = False  # Signal to exit main loop

        elif event.type == pygame.VIDEORESIZE:  # Handle window resize events
            new_size = (max(windowMinWidth, event.w), max(windowMinHeight, event.h))
            windowSurface = pygame.display.set_mode(new_size, pygame.RESIZABLE)
            windowSurface.fill(BG_COLOUR)
            manager.set_window_resolution(new_size)

            # Recreate UI elements because clear_and_reset() destroys them
            manager.clear_and_reset()
            _create_dialog_label(new_size)

            # Restore and refit the last text for the new box size
            if dialog_text_last:
                gui_print(dialog_text_last)

        manager.process_events(event)  # Pass event to UI manager for UI-specific handling

    windowSurface.fill(BG_COLOUR)  # Clear window each frame to prevent ghosting/overdraw

    manager.update(timeDelta)  # Update UI manager state, animations, and transitions
    manager.draw_ui(windowSurface)  # Draw all managed UI elements onto window surface
    
    # Devtools overlay (toggle by commenting this out)
    # DEVTOOLS()

    pygame.display.flip()  # Update the entire display to show latest rendered frame

    return running  # Return whether the main loop should continue


# Devtools function for mouse coordinate label (depends on manager global)
def DEVTOOLS():
    """Draw small debug aids (mouse coords and the DialogLabel bounds)."""
    # Shows mouse coordinates in top-left corner
    global mouse_label, DialogLabel, windowSurface
    if mouse_label is None:
        mouse_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(10, 10, 160, 24),  # x, y, width, height
            text="x:0 y:0",
            manager=manager,
            anchors={"left": "left", "top": "top"}
        )
    mx, my = pygame.mouse.get_pos()
    mouse_label.set_text(f"x:{mx} y:{my}")

    # Shows hitbox of DialogLabel
    if DialogLabel is not None:
        pygame.draw.rect(
            windowSurface,
            BORDER_COLOUR,  # Red border
            DialogLabel.rect,
            2  # Border thickness
        )
