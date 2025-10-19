# Coding standards -
# Variables must be in camelCase 
# Functions must be in snake_case

from gui import * 
from gameParser import *
#need to import player module


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

main()
