from items import *
from dungeon_map import *
peasant = {
    "health": 100,
    "damageMult": 1,
    "maxWeight": 2.5,
    "mana": 100
    }
barbarian = {
    "health": 250,
    "damageMult": 1,
    "maxWeight": 8,
    "mana": 100
    }
archer = {
    "health": 125,
    "damageMult": 1.75,
    "maxWeight": 5

    }
mage = {
    "health": 150,
    "damageMult": 1,
    "maxWeight": 3.5,
    "mana": 100
    }
#defines all classes and their different perks/drawbacks (more to be added)

playerClass = peasant
#sets the players starting class as peasant

inventory = []
#sets starting inventory

currentRoom = rooms["kidnapped_cell"]
currentWeapon = item_fighter_longsword
