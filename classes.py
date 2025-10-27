from items import *
from dungeon_map import *
peasant = {
    "health": 100,
    "damageMult": 1,
    "maxWeight": 2.5,
    "mana": 100,
    "starterItems": []}
barbarian = {
    "health": 250,
    "damageMult": 1,
    "maxWeight": 8,
    "mana": 100,
    "starterItems": [item_fighter_shortsword, item_shield_wood, item_armor_leather_set]
    }
archer = {
    "health": 125,
    "damageMult": 1.75,
    "maxWeight": 5,
    "mana": 100,
    "starterItems": [item_archer_shortbow, item_quiver_arrows, item_armor_leather_set]

    }
mage = {
    "health": 150,
    "damageMult": 1,
    "maxWeight": 3.5,
    "mana": 100,
    "starterItems": [item_mage_oak_staff, item_armor_mage_robes]
    }
#defines all classes and their different perks/drawbacks (more to be added)

playerClass = peasant
#sets the players starting class as peasant

inventory = []
#sets starting inventory

currentRoom = rooms["kidnapped_cell"]
currentWeapon = item_fighter_longsword
currentArmor = item_armor_leather_set
