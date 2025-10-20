# Leave to James


import sys
import pygame # type: ignore
import pygame_gui # type: ignore

# --- Module state (globals) ---
windowSurface = None
manager = None
clock = None
running = False
windowMinWidth = 640
windowMinHeight = 480
windowSize = None
mouse_label = None  # keep DEVTOOLS compatibility
DialogLabel = None  # will hold the always-present centre label


def start():
    """Initialize pygame, create window, UI manager, and always-present dialog label."""
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
    windowSurface.fill((30, 30, 36))
    pygame.display.flip()

    # Create UI manager with current window size
    manager = pygame_gui.UIManager(windowSize)

    # Create a centered UILabel with empty text to always exist
    DialogLabel = pygame_gui.elements.UITextBox(
        html_text='',
        relative_rect=pygame.Rect(0, 0, 1000, 500),
        manager=manager,
        anchors={"centerx": "centerx", "centery": "centery"}
    )

    running = True  # Set running flag to True to start event loop


def gui_print(text):
    """Update the always-present dialog label text."""
    global DialogLabel
    # Update label text or clear if None/empty
    if DialogLabel is not None:
        DialogLabel.set_text(text or "")


def pump():
    """Process one frame of events and UI update. Return running state."""
    global running, windowSurface, manager

    timeDelta = clock.tick(60) / 1000.0  # Limit frame rate to 60 FPS and get elapsed time in seconds

    for event in pygame.event.get():  # Process all events in the event queue
        if event.type == pygame.QUIT:  # Check if the user has requested to close the window
            running = False  # Signal to exit main loop

        elif event.type == pygame.VIDEORESIZE:  # Handle window resize events
            new_size = (max(windowMinWidth, event.w), max(windowMinHeight, event.h))  # Enforce minimum window size
            windowSurface = pygame.display.set_mode(new_size, pygame.RESIZABLE)  # Resize window surface
            windowSurface.fill((30, 30, 36))  # Clear resized window with background color
            manager.set_window_resolution(new_size)  # Inform UI manager of new window size
            manager.clear_and_reset()  # Reset UI elements for new size

        manager.process_events(event)  # Pass event to UI manager for UI-specific handling

    windowSurface.fill((30, 30, 36))  # Clear window each frame to prevent ghosting/overdraw

    manager.update(timeDelta)  # Update UI manager state, animations, and transitions
    manager.draw_ui(windowSurface)  # Draw all managed UI elements onto window surface
    
    DEVTOOLS() #Uncomment this line to enable devtools

    pygame.display.flip()  # Update the entire display to show latest rendered frame

    return running  # Return whether the main loop should continue


# Devtools function for mouse coordinate label (depends on manager global)
def DEVTOOLS():
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
    pygame.draw.rect(
        windowSurface,
        (255, 0, 0),  # Red border
        DialogLabel.rect,
        2  # Border thickness
    )
