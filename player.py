from items import *
peasant = {
    "health": 100,
    "damageMult": 1,
    "maxWeight": 2.5

    }
barbarian = {
    "health": 250,
    "damageMult": 1,
    "maxWeight": 8

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

inventory = [item_archer_longbow, item_fighter_longsword, item_shield_wood, item_armor_leather_set, item_potion_mana_small, item_potion_health_medium]
#sets starting inventory

currentRoom = '''add when map is made'''
