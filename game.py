#---------------


# Coding standards -
# Variables must be in camelCase 
# Functions must be in snake_case
# Add comments to as many lines as possible to explain the code to other devs


#---------------

import gui


# Main game loop
def main():
    # Initialize the GUI window and setup necessary resources
    gui.start()
    # Continuously run the game loop while the GUI is responsive
    while True:
        # Update the text displayed in the GUI
        gui.gui_print("You are in a maze of twisty little passages, all alike. Next to you is the School of Computer Science and Informatics reception. The receptionist, Matt Strangis, seems to be playing an old school text-based adventure game on his computer. There are corridors leading to the south and east. The exit is to the west. <BLANKLINE> There is a pack of biscuits, a student handbook here. <BLANKLINE>")
        # Pump the GUI to keep it responsive and process events
        if not gui.pump():
            # Exit the loop if the GUI is closed or no longer responsive
            break


main()