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
from dungeon_map import *
import time
#need to import player module




import gui



def print_directions(exits):
    ''' itterate through all available exits and output them
    must wait until map is done and exits are in place'''
    for ex in exits:
            gui.gui_print("GO", ex,"to Travel to", exits[ex])

# Main game loop
def valid_exit(exits, chosenExit):
    return chosenExit in exits

def move_player(direction, currentRoom):
    if valid_exit(currentRoom["exits"], direction)==True:
        currentRoom=rooms[currentRoom][direction]
    else:
        gui.gui_print("That way is blocked!")
    return currentRoom
    #changes the global var currentRoom to the room pointed to in the dictionary
def get_mass():
    mass = 0
    for item in inventory:
        mass = mass+item["mass"]
    return mass
    #returns the mass of the total items in the players inventory


def print_inventory():
    invMass = get_mass()
    gui.gui_print("PLAYER INVENTORY",invMass,"/",playerClass["maxWeight"],"KG")
    #outputs the title inventory and how much space is left
    gui.gui_print("==============================")
    gui.gui_print()
    for item in inventory:
    
        gui.gui_print(item["name"].upper()+"(",item["mass"],"kg)")
        
        if item["type"]=="weapon":
            gui.gui_print("DMG:",item["damage"])
        elif item["type"]=="armor":
            gui.gui_print("BLOCK:",item["block"])
        elif item["type"]=="shield":
            gui.gui_print("BLOCK:",item["block"])
        elif item["type"]=="health_potion":
            gui.gui_print("RESTORATION:",item["restore_hp"],"HEALTH")
        elif item["type"]=="mana_potion":
            gui.gui_print("RESTORATION:",item["restore_mana"],"MANA")
        gui.gui_print()
        #finds out the type of each item and outputs appropriate stats for them
        #can be changed to output more stats later
                

#All these functions check what the item is in inventory to decide the appropriate output
def execute_take(item_id, currentRoom, playerClass):
    gui.gui_print(item_id)
    room_items = currentRoom["items"]
    #sets a variable for the items the room holds
    mass = get_mass(inventory)
    #gets the current mass of all items in inventory
    for i in room_items:
        if item_id == i["id"] and not item_id in inventory:
            #if the item the player input is in the room and not in the players inventory
            if i["mass"]+mass<=playerClass[maxWeight]:
                #if the object wont make the players inventory weigh more than the max capacity then it will pick it up
                inventory.append(i)
                #adds item to inventory
                currentRoom["items"].remove(i)
                #removes item from room
                gui.gui_print("You have taken", item_id)
            else:
                gui.gui_print("That is too heavy to carry!")
        else:
            gui.gui_print("That is not a valid item to take in this room!!")
    
    
def execute_drop(item_id, currentRoom):
   
    for i in inventory:
        if item_id == i["id"] and not item_id in currentRoom["items"]:
            #if the item input is the same the id and not already in the room
            currentRoom["items"].append(i)
            #add the item to the room items
            inventory.remove(i)
            #removes item from inventory
            gui.gui_print("You have dropped", item_id,"in",currentRoom["name"])
            
def execute_go(direction, currentRoom):
    
    nextRoom = move(currentRoom["exits"], direction)
    #gets the next room to move too
    if nextRoom:
        #if the room is valid
        currentRoom = nextRoom
        #the current room becomes the next room
        
    else:
        gui.gui_print("That is not a valid direction for an exit!!")
    print_current_room(currentRoom)
    #outputs
    return currentRoom
    
        
   
def execute_command(command, currentRoom, playerClass):
    if 0 == len(command):
        gui.gui_print("You must enter an input")
        return
    if command[0] == "open":
        #when the first word input is open these will run
        if len(command) > 1:
            if command[1]== "inventory":
            #if the following word is inventory it outputs the players current inventory
                print_inventory()
            elif command[1]== "map":
                #if the following word is map it outputs the players next exits available
                print_directions(currentRoom["exits"])
            elif command[1]== "stats":
                #if the following word is stats it outputs the players stats
                print_stats(playerClass)
        else:
            gui.gui_print("Open what??")
        
        

    elif command[0] == "go":
        #if the initial word is go it will run this
        if len(command) > 1:
            currentRoom = execute_go(command[1], currentRoom)
            #changes the current room variable to the output of the execute_go function
        else:
            gui.gui_print("Go where?")
    else:
        gui.gui_print("This makes no sense.")
    return currentRoom

'''
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], currentRoom, playerClass)
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1], currentRoom)
        else:
            print("Drop what?")
'''


   
def move(exits, direction):
    # Next room to go to
    if direction in exits:
        return rooms[exits[direction]]

def print_current_room(currentRoom):
    gui.gui_print()
    gui.gui_print("Location:", currentRoom["name"])
    gui.gui_print(currentRoom["description"])
    #outputs name and description of a room

def get_user_input():
    userChoice = gui.get_text_input("What would you like to do? ")
    normalised = normalise_input(userChoice)
    #returns normalised text as an array of words
    gui.gui_print()
    return normalised
    #gets input and normalises it
def print_menu(currentRoom):
    exitString = get_exits(currentRoom["exits"])
    gui.gui_print()
    gui.gui_print("You can:")
    gui.gui_print()
    gui.gui_print("||OPEN INVENT0RY||  ||OPEN MAP|| ||OPEN STATS||")
    gui.gui_print(exitString)
    
def get_exits(exits):
    string = ""
    for i in exits:
        string = string+"|| "+"GO "+i.upper()+" ||  "
    return string
def menu(currentRoom):
    print_menu(currentRoom)
    userInput = get_user_input()
    currentRoom = execute_command(userInput, currentRoom, playerClass)
    return currentRoom

def open_game(currentRoom, playerClass):
    gui.gui_print("WELCOME")
    gui.gui_print("Press ENTER to start")
    enterToStart = gui.get_text_input()
    print_current_room(currentRoom)
    while playerClass== peasant:
        playerClass = class_choice(playerClass)
    gui.gui_print("Good choice")
    gui.gui_print("STATS:")
    gui.gui_print(playerClass)
    print_stats(playerClass)
    #runs the opeining game sequence
    return playerClass
#runs the main game menu

def print_stats(playerClass):
    gui.gui_print()
    gui.gui_print("HEALTH:",playerClass["health"])
    gui.gui_print()
    gui.gui_print("Damage multiplier:", playerClass["damageMult"],"X")
    gui.gui_print()
def class_choice(playerClass):
    gui.gui_print()
    gui.gui_print("Infront of you the wall shows 3 armour stands. One bears a large hulking armour that can withstand many strikes, one bears a light leather uniform designed for speed and deadlyness, and the final stand holds a robe that emmits magical properties:")
    gui.gui_print("Choose either the BARBARIAN, ARCHER OR MAGE:")
    choice = gui.get_text_input()
    #gets the users input on what class they wish to pick
    normChoice = normalise_input(choice)
    if normChoice[0]=="barbarian":
        playerClass = barbarian
    elif normChoice[0]=="archer":
        playerClass = archer
    elif normChoice[0]=="mage":
        playerClass = mage
    else:
        gui.gui_print("That is not a class")
    #changes the players class and returns what they have picked
    return playerClass

        
def main(currentRoom, playerClass):
    # Initialize the GUI window and setup necessary resources
    gui.start()
    
    playerClass = open_game(currentRoom, playerClass)
    #runs the opening function at the start of the game
    
    # Continuously run the game loop while the GUI is responsive
    while True:
        gui.gui_print(playerClass)
        currentRoom = menu(currentRoom)
        # Update the text displayed in the GUI
        
        # Pump the GUI to keep it responsive and process events
        if not gui.pump():
            # Exit the loop if the GUI is closed or no longer responsive
            break


main(currentRoom, playerClass)

