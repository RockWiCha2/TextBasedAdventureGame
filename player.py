from items import *
from dungeon_map import *
peasant = {
    "health": 100,
    "damageMult": 1,
    "maxWeight": 2.5,
    "description": "A simple villager with no training. Weak, but full of determination."
    

    }
barbarian = {
    "health": 250,
    "damageMult": 1,
    "maxWeight": 8,
    "description": "A savage warrior with immense strength and stamina."

    }
archer = {
    "health": 125,
    "damageMult": 1.75,
    "maxWeight": 5,
    "description": "A skilled hunter who strikes swiftly from a distance."

    }
mage = {
    "health": 150,
    "damageMult": 1,
    "maxWeight": 3.5,
    "mana": 100,
    "description": "A wise spellcaster who uses magic to defeat enemies."
    }
#defines all classes and their different perks/drawbacks (more to be added)

playerClass = peasant
#sets the players starting class as peasant

inventory = [item_archer_longbow, item_fighter_longsword, item_shield_wood, item_armor_leather_set, item_potion_mana_small, item_potion_health_medium]
#sets starting inventory

currentRoom = rooms["sealed_gate"]
