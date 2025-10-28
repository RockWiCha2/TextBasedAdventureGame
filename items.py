# Fantasy Items (Weapons, Spells, Armour, Potions, Keys) 


# Fighter weapons
fist_attack = {
    "id": "punch",
    "name": "a punch",
    "description": "left right goodnight",
    "mass": 0.8,
    "type": "weapon",
    "class": "peasant",
    "damage": 10
}
item_fighter_shortsword = {
    "id": "shortsword",
    "name": "a shortsword",
    "description": "A balanced shortsword, easy to handle.",
    "mass": 0.8,
    "type": "weapon",
    "class": "fighter",
    "damage": 30
}

item_fighter_longsword = {
    "id": "longsword",
    "name": "a longsword",
    "description": "A reliable steel longsword.",
    "mass": 1.0,
    "type": "weapon",
    "class": "fighter",
    "damage": 40
}

item_fighter_greatsword = {
    "id": "greatsword",
    "name": "a greatsword",
    "description": "A hefty two-handed blade.",
    "mass": 1.4,
    "type": "weapon",
    "class": "fighter",
    "damage": 70
}

# Shields
item_shield_wood = {
    "id": "woodshield",
    "name": "a wooden shield",
    "description": "A round shield made of reinforced oak.",
    "mass": 0.6,
    "type": "shield",
    "block": 15
}

item_shield_iron = {
    "id": "ironshield",
    "name": "an iron shield",
    "description": "A sturdy iron shield with a boss.",
    "mass": 0.8,
    "type": "shield",
    "block": 25
}

# Archer weapons and ammo
item_archer_shortbow = {
    "id": "shortbow",
    "name": "a shortbow",
    "description": "Light bow suited for quick shots.",
    "mass": 0.7,
    "type": "weapon",
    "class": "archer",
    "damage": 30
}

item_archer_longbow = {
    "id": "longbow",
    "name": "a longbow",
    "description": "Tall yew bow with great range.",
    "mass": 0.9,
    "type": "weapon",
    "class": "archer",
    "damage": 50
}

item_archer_light_crossbow = {
    "id": "lightcrossbow",
    "name": "a light crossbow",
    "description": "Simple crossbow, easy to maintain.",
    "mass": 1.0,
    "type": "weapon",
    "class": "archer",
    "damage": 80
}

item_quiver_arrows = {
    "id": "arrows",
    "name": "a quiver of arrows",
    "description": "A leather quiver holding 20 arrows.",
    "mass": 0.3,
    "type": "ammo",
    "ammo_type": "arrow",
    "ammo": 20
}

# Mage staves
item_mage_oak_staff = {
    "id": "oakstaff",
    "name": "an oak staff",
    "description": "A simple staff channeling basic energies.",
    "mass": 0.7,
    "type": "weapon",
    "class": "mage",
    "damage": 10,
    "spell_power": 1
}

item_mage_runed_staff = {
    "id": "runedstaff",
    "name": "a runed staff",
    "description": "A staff etched with arcane runes.",
    "mass": 0.9,
    "type": "weapon",
    "class": "mage",
    "damage": 15,
    "spell_power": 2
}

item_mage_arcane_staff = {
    "id": "arcanestaff",
    "name": "an arcane staff",
    "description": "A masterwork staff humming with power.",
    "mass": 1.1,
    "type": "weapon",
    "class": "mage",
    "damage": 20,
    "spell_power": 3
}

# Spells (as items the mage can learn/use)
item_spell_firebolt = {
    "id": "firebolt",
    "name": "Firebolt",
    "description": "Launch a bolt of fire at a target.",
    "mass": 0.1,
    "type": "spell",
    "element": "fire",
    "damage": 40,
    "mana_cost": 5
}

item_spell_icespike = {
    "id": "icespike",
    "name": "Ice Spike",
    "description": "Hurl a shard of ice that slows foes.",
    "mass": 0.1,
    "type": "spell",
    "element": "ice",
    "damage": 60,
    "mana_cost": 5,
    "effect": "slow"
}

item_spell_lightning = {
    "id": "lightning",
    "name": "Lightning Bolt",
    "description": "Strike an enemy with crackling lightning.",
    "mass": 0.1,
    "type": "spell",
    "element": "lightning",
    "damage": 80,
    "mana_cost": 8
}

item_spell_heal = {
    "id": "heal",
    "name": "Healing Word",
    "description": "Mend wounds with a whispered prayer.",
    "mass": 0.1,
    "type": "spell",
    "heal": 20,
    "mana_cost": 6
}

# Armour sets
item_armor_iron_set = {
    "id": "ironarmor",
    "name": "a set of iron armor",
    "description": "Chain and plate offering solid protection.",
    "mass": 1.0,
    "type": "armor",
    "class": "fighter",
    "block": 50
}

item_armor_leather_set = {
    "id": "leatherarmor",
    "name": "a set of leather armor",
    "description": "Hardened leather, light and quiet.",
    "mass": 0.8,
    "type": "armor",
    "class": "archer",
    "block": 30
}

item_armor_mage_robes = {
    "id": "magesrobes",
    "name": "a set of mage robes",
    "description": "Enchanted robes aiding spellcasting.",
    "mass": 0.6,
    "type": "armor",
    "class": "mage",
    "block": 20,
    "mana_bonus": 10
}

# Potions
item_potion_health_small = {
    "id": "hpotions",
    "name": "a small health potion",
    "description": "Restores a small amount of vitality.",
    "mass": 0.2,
    "type": "health_potion",
    "restore_hp": 15
}

item_potion_health_medium = {
    "id": "hpotionsm",
    "name": "a medium health potion",
    "description": "Restores a fair amount of vitality.",
    "mass": 0.4,
    "type": "health_potion",
    "restore_hp": 30
}

item_potion_mana_small = {
    "id": "mpotions",
    "name": "a small mana potion",
    "description": "Restores a small amount of mana.",
    "mass": 0.2,
    "type": "mana_potion",
    "restore_mana": 10
}

item_potion_mana_medium = {
    "id": "mpotionsm",
    "name": "a medium mana potion",
    "description": "Restores a fair amount of mana.",
    "mass": 0.4,
    "type": "mana_potion",
    "restore_mana": 25
}

# Key items
item_witchs_charm = {
    "id": "charm",
    "name": "a witch charm",
    "description": "A small, twisted effigy made of wicker and raven feathers. It hums with a strange, dark energy.",
    "mass": 0.1,
    "type": "key"
}

item_knights_crest = {
    "id": "crest",
    "name": "a knight crest",
    "description": "A heavy steel emblem, warm to the touch. It represents a solemn vow to guard the kingdom.",
    "mass": 0.2,
    "type": "key"
}

# Starter gear bundles for class choice
fighter_starter_set = [
    item_fighter_longsword, item_shield_iron, item_armor_iron_set
]

archer_starter_set = [
    item_archer_longbow, item_quiver_arrows, item_armor_leather_set
]

mage_starter_set = [
    item_mage_runed_staff, item_spell_firebolt, item_spell_heal, item_armor_mage_robes
]

# Optional catalogs
items_weapons = [
    item_fighter_shortsword, item_fighter_longsword, item_fighter_greatsword,
    item_shield_wood, item_shield_iron, item_archer_shortbow,
    item_archer_longbow, item_archer_light_crossbow, item_mage_oak_staff,
    item_mage_runed_staff, item_mage_arcane_staff
]

items_spells = [
    item_spell_firebolt, item_spell_icespike, item_spell_lightning, item_spell_heal
]

items_armours = [
    item_armor_iron_set, item_armor_leather_set, item_armor_mage_robes
]

items_potions = [
    item_potion_health_small, item_potion_health_medium,
    item_potion_mana_small, item_potion_mana_medium
]

items_keys = [item_witchs_charm, item_knights_crest]

# Convenience list of all fantasy items
fantasy_items = items_weapons + items_spells + items_armours + items_potions + items_keys + [item_quiver_arrows]
