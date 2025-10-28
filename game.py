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
from players import *
from dungeon_map import *
from classes import *
from combat import *
from enemies import *
import time
#need to import player module




import gui



def print_directions(exits):
    ''' itterate through all available exits and output them
    must wait until map is done and exits are in place'''
    string = ""
    for ex in exits:
            string = string+"GO "+ ex+" to Travel to "+ exits[ex]+"\n"
    gui.gui_print(string+"Press enter to continue")
    _ = gui.get_text_input()
# Main game loop
def valid_exit(exits, chosenExit):
    return chosenExit in exits

def move_player(direction, currentRoom):
    if valid_exit(currentRoom["exits"], direction)==True:
        currentRoom=rooms[currentRoom][direction]
    else:
        print("That way is blocked!")
    return currentRoom
    #changes the global var currentRoom to the room pointed to in the dictionary
def get_mass(inventory):
    mass = 0
    for item in inventory:
        mass = mass+item["mass"]
    return mass
    #returns the mass of the total items in the players inventory


def print_inventory():
    invMass = get_mass(inventory)
    #outputs the title inventory and how much space is left
    string = ""
    for item in inventory:
    
        string = string+(item["name"].upper()+"(",item["mass"],"kg)")
        
        if item["type"]=="weapon":
            string = string+("DMG:",item["damage"])
        elif item["type"]=="armor":
            string = string+("BLOCK:",item["block"])
        elif item["type"]=="shield":
            string = string+("BLOCK:",item["block"])
        elif item["type"]=="health_potion":
            string = string+("RESTORATION:",item["restore_hp"],"HEALTH")
        elif item["type"]=="mana_potion":
            string = string+("RESTORATION:",item["restore_mana"],"MANA")
        string = string,"\n"
    
    gui.gui_print("PLAYER INVENTORY" + "\n" +string+"\n"+"Press enter to continue")
    
    _ = gui.get_text_input()
        #finds out the type of each item and outputs appropriate stats for them
        #can be changed to output more stats later
                

#All these functions check what the item is in inventory to decide the appropriate output
def execute_take(item_id, currentRoom, playerClass):
    print(item_id)
    room_items = currentRoom["items"]
    #sets a variable for the items the room holds
    mass = get_mass(inventory)
    #gets the current mass of all items in inventory
    for i in room_items:
        if item_id == i["id"] and not item_id in inventory:
            #if the item the player input is in the room and not in the players inventory
            if i["mass"]+mass<=playerClass["maxWeight"]:
                #if the object wont make the players inventory weigh more than the max capacity then it will pick it up
                if i["class"]==playerClass:
                    inventory.append(i)
                    #adds item to inventory
                    currentRoom["items"].remove(i)
                    #removes item from room
                    print("You have taken", item_id)
            else:
                print("That is too heavy to carry!")
        else:
            print("That is not a valid item to take in this room!!")

def check_for_keys(inventory):
    # Checks if both the Knight's Crest and Witch's Charm are in the inventory.
    has_crest = False
    has_charm = False

    # Loop through the inventory to find the keys
    for item in inventory:
        if item["id"] == "crest":  #
            has_crest = True
        elif item["id"] == "charm":  #
            has_charm = True

    # Return True only if both keys were found
    return has_crest and has_charm
   
def execute_command(command, currentRoom, playerClass):
    if 0 == len(command):
        print("You must enter an input")
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
            print("Open what??")
        
        

    elif command[0] == "go":
        if len(command) > 1:
            direction = command[1]
            next_room = move(currentRoom["exits"], direction)  # Find the next room

            if next_room:
                # Check if the destination is the Dragon's Lair
                if next_room == rooms["dragon_lair"]:
                    # If it is, check if the player has the keys
                    if not check_for_keys(inventory):
                        # If keys are missing, block entry and don't change the room
                        gui.gui_print(
                            "The massive door is sealed by a powerful magic. You feel the presence of two forces, one of honor and one of darkness, barring your way.")
                    else:
                        # If keys are present, allow movement
                        gui.gui_print(f"You travel {direction}...")
                        currentRoom = next_room
                else:
                    # For any other room, allow movement
                    gui.gui_print(f"You travel {direction}...")
                    currentRoom = next_room
            else:
                gui.gui_print("That is not a valid direction for an exit!!")
        else:
            gui.gui_print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            # Join all words after "take" to get the full item name
            item_name_to_take = " ".join(command[1:])

            item_found = None  # Variable to hold the item if we find it

            # Loop through all items in the current room
            for item in currentRoom["items"]:
                # Check if the name you typed is part of the item's descriptive name
                if item_name_to_take.lower() in item["name"].lower():
                    item_found = item
                    break  # Stop searching once we find a match

            if item_found:
                current_mass = get_mass(inventory)
                # Check if the player has enough capacity to carry the item
                if (current_mass + item_found["mass"]) <= playerClass["maxWeight"]:
                    inventory.append(item_found)
                    currentRoom["items"].remove(item_found)
                    gui.gui_print(f"You have taken {item_found['name']}.")
                else:
                    gui.gui_print("That is too heavy to carry!")
            else:
                # This message now only shows if the item truly isn't in the room
                gui.gui_print("There is no such item here.")
        else:
            gui.gui_print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            # Join all words after "drop" to get the full item name
            item_name_to_drop = " ".join(command[1:])

            item_found = None  # Variable to hold the item if we find it

            # Loop through all items in the player's inventory
            for item in inventory:
                # Remove punctuation for a fair comparison
                item_name_in_inventory = remove_punct(item["name"].lower())

                # Check if the name that has been is part of the item's full name
                if item_name_to_drop.lower() in item_name_in_inventory:
                    item_found = item
                    break  # Stop searching once we find a match

            if item_found:
                # Move the item from the inventory to the room
                currentRoom["items"].append(item_found)
                inventory.remove(item_found)
                gui.gui_print(f"You have dropped {item_found['name']}.")
            else:
                gui.gui_print("You don't have that item in your inventory.")
        else:
            gui.gui_print("Drop what?")
    else:
        print("This makes no sense.")

    return currentRoom, playerClass

   
def move(exits, direction):
    # Next room to go to
    if direction in exits:
        return rooms[exits[direction]]

def print_current_room(currentRoom):
    
    gui.gui_print("Location: " + currentRoom["name"] + "\n" + currentRoom["description"])
    #outputs name and description of a room

def get_user_input():
    userChoice = gui.get_text_input()
    normalised = normalise_input(userChoice)
    #returns normalised text as an array of words
    
    return normalised
    #gets input and normalises it
def print_menu(currentRoom):
    exitString = get_exits(currentRoom["exits"])
    takeString = get_take(currentRoom["items"])
    dropString = get_drop(inventory)
    gui.gui_print("You can:\n||OPEN INVENT0RY||\n||OPEN MAP||\n||OPEN STATS||\n" + exitString + "\n" + takeString + "\n" + dropString)
def get_exits(exits):
    string = ""
    for i in exits:
        string = string+"|| "+"GO "+i.upper()+" ||  "
    return string
def get_drop(inventory):
    string = ""
    for i in inventory:
        string = string+"|| "+"DROP "+i["name"].upper()+" ||  "
    return string
def get_take(items):
    string = ""
    for i in items:
        string = string+"|| "+"TAKE "+i["name"].upper()+" ||  "
    return string

def menu(currentRoom, playerClass):
    exitString = get_exits(currentRoom["exits"])
    takeString = get_take(currentRoom["items"])
    dropString = get_drop(inventory)

    combined_message = (
        f"Location: {currentRoom['name']}\n"
        f"{currentRoom['description']}\n\n"
        "You can:\n"
        "||OPEN INVENT0RY||  ||OPEN MAP||  ||OPEN STATS||\n"
        f"{exitString}\n{takeString}\n{dropString}"
    )

    gui.gui_print(combined_message)
    userInput = get_user_input()
    currentRoom, playerClass = execute_command(userInput, currentRoom, playerClass)
    return currentRoom, playerClass

def open_game(currentRoom, playerClass):
    gui.gui_print("WELCOME\nPress ENTER to start")
    _ = gui.get_text_input()
    print_current_room(currentRoom)
    #runs the opeining game sequence
    
#runs the main game menu

def print_stats(playerClass):
    hstring = f"HEALTH: {playerClass['health']}"
    dstring = f"Damage multiplier: {playerClass['damageMult']}"
    gui.gui_print(hstring + "\n" + dstring + "X\nPress enter to continue")
    _ = gui.get_text_input()



    
def class_choice(playerClass):
    
    gui.gui_print("Infront of you the wall shows 3 armour stands. One bears a large hulking armour that can withstand many strikes, one bears a light leather uniform designed for speed and deadlyness, and the final stand holds a robe that emmits magical properties:"+"\n"+"Choose either the BARBARIAN, ARCHER OR MAGE:")
    
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

def class_pick(playerClass, inventory):
    while playerClass== peasant:
        playerClass = class_choice(playerClass)
    for i in playerClass["starterItems"]:
            inventory.append(i)
    print("Good choice")
    print("STATS:")
    print_stats(playerClass)
    return playerClass, inventory
def main(currentRoom, playerClass, inventory):
    # Initialize the GUI window and setup necessary resources
    pickedClass = False
    gui.start()
    gui.pump()
    open_game(currentRoom, playerClass)
    while True:
        
        currentRoom, playerClass = menu(currentRoom, playerClass)
        if currentRoom["enemy"]!=None:
            start_encounter(playerClass, currentRoom["enemy"])
            currentRoom["enemy"] = None
        if currentRoom == rooms["armory"]and pickedClass==False:
            playerClass, inventory = class_pick(playerClass, inventory)
            pickedClass = True
            
    '''
    gui.start()
    
    playerClass = open_game(currentRoom, playerClass)
    #runs the opening function at the start of the game
    
    # Continuously run the game loop while the GUI is responsive
    while True:
        print(playerClass)
        currentRoom = menu(currentRoom)
        # Update the text displayed in the GUI
        
        # Pump the GUI to keep it responsive and process events
        if not gui.pump():
            # Exit the loop if the GUI is closed or no longer responsive
            break
    '''

main(currentRoom, playerClass, inventory)

