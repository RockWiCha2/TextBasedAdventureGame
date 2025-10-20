#---------------


# Coding standards -
# Variables must be in camelCase 
# Functions must be in snake_case
# Add comments to as many lines as possible to explain the code to other devs
# Check requirements.txt to see what libraries/modules you need to install


#---------------
from gui import * 
from gameParser import *
#need to import player module




import gui



def print_directions(exits):
    ''' itterate through all available exits and output them
    must wait until map is done and exits are in place'''
    ''' for ex in exits:
            print("GO", ex,"to Travel to", exits[ex])
        or something similiar'''

# Main game loop

def print_inventory():
    '''
    for item in inventory:
        print(item["name"].upper())
        print(other stats when items are added)

    '''
def print_current_room():
    '''print("Location:", rooms[currentRoom]["name"])
    print(rooms[currentRoom[description]])
    '''

def get_user_input():
    userChoice = input("What would you like to do? ")
    normalised = normalise_input(userChoice)
    print(normalised)
    return normalised

def print_menu():
    print_directions
    
def menu():
    print_menu()
    userInput = get_user_input()
    
def main():
    while True:
        #Call functions for game logic here
        menu()

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
