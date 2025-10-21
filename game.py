"""
---------------


# Coding standards -
# Variables must be in camelCase 
# Functions must be in snake_case
# Add comments to as many lines as possible to explain the code to other devs
# Check requirements.txt to see what libraries/modules you need to install


---------------
"""

from gui import * 
from gameParser import *
from items import *
from player import *
import time
#need to import player module




import gui



def print_directions(exits):
    ''' itterate through all available exits and output them
    must wait until map is done and exits are in place'''
    ''' for ex in exits:
            print("GO", ex,"to Travel to", exits[ex])
        or something similiar'''

# Main game loop
def get_mass():
    mass = 0
    for item in inventory:
        mass = mass+item["mass"]
    return mass
    #returns the mass of the total items in the players inventory


def print_inventory():
    invMass = get_mass()
    print("PLAYER INVENTORY",invMass,"/",playerClass["maxWeight"])
    #outputs the title inventory and how much space is left
    print("==============================")
    print()
    for item in inventory:
    
        print(item["name"].upper()+"(",item["mass"],"kg)")
        
        if item["type"]=="weapon":
            print("DMG:",item["damage"])
        elif item["type"]=="armor":
            print("BLOCK:",item["block"])
        elif item["type"]=="shield":
            print("BLOCK:",item["block"])
        elif item["type"]=="health_potion":
            print("RESTORATION:",item["restore_hp"],"HEALTH")
        elif item["type"]=="mana_potion":
            print("RESTORATION:",item["restore_mana"],"MANA")
        print()
        #finds out the type of each item and outputs appropriate stats for them
        #can be changed to output more stats later
                

#All these functions check what the item is in inventory to decide the appropriate output

def execute_command(command):
    if 0 == len(command):
        return
    if command[0] == "inventory":
        print_inventory()
        #if the players input is inventory it opens the inventory 
'''
    if command[0] == "go":
        if len(command) > 1:
            current_room = execute_go(command[1], current_room)
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], current_room)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1], current_room)
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")
    if current_room:
        return current_room
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
    #gets input and normalises it
def print_menu():
    print_directions
    
def menu():
    print_menu()
    userInput = get_user_input()
    execute_command(userInput)
    #runs the main game menu
def main():
    
    # Initialize the GUI window and setup necessary resources
    gui.start()
    # Continuously run the game loop while the GUI is responsive
    while True:
        
        # Update the text displayed in the GUI
        gui.gui_print("You are in a maze of twisty little passages, all alike. Next to you is the School of Computer Science and Informatics reception. The receptionist, Matt Strangis, seems to be playing an old school text-based adventure game on his computer. There are corridors leading to the south and east. The exit is to the west. There is a pack of biscuits, a student handbook here.")
        
        # Pump the GUI to keep it responsive and process events
        if not gui.pump():
            # Exit the loop if the GUI is closed or no longer responsive
            break


main()
