from items import *
from dungeon_map import *
peasant = {
    "name": "peasant",
    "health": 100,
    "damageMult": 1,
    "maxWeight": 2.5,
    "mana": 100,
    "starterItems": []}
barbarian = {
    "name": "barbarian",
    "health": 250,
    "damageMult": 1,
    "maxWeight": 20,
    "mana": 100,
    "starterItems": [item_fighter_shortsword, item_shield_wood, item_armor_leather_set]
    }
archer = {
    "name": "archer",
    "health": 125,
    "damageMult": 1.75,
    "maxWeight": 20,
    "mana": 100,
    "starterItems": [item_archer_shortbow, item_quiver_arrows, item_armor_leather_set]

    }
mage = {
    "name": "mage",
    "health": 150,
    "damageMult": 1,
    "maxWeight": 20,
    "mana": 100,
    "starterItems": [item_mage_oak_staff,
                     item_armor_mage_robes,
                     item_spell_firebolt,
                     item_spell_heal,
                     ]
    }
#defines all classes and their different perks/drawbacks (more to be added)

playerClass = peasant
#sets the players starting class as peasant

inventory = []
#sets starting inventory

currentRoom = rooms["kidnapped_cell"]
currentWeapon = item_fighter_longsword
currentArmor = item_armor_leather_set
