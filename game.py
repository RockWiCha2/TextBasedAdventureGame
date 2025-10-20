#---------------


# Coding standards -
# Variables must be in camelCase 
# Functions must be in snake_case
# Add comments to as many lines as possible to explain the code to other devs


#---------------

import gui


# Main game loop
def main():
    gui.start()
    while True:
        gui.gui_print("Welcome to the adventure")
        # Call functions for game logic here
        pass  # Placeholder to avoid syntax error


main()