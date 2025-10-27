from items import *
from enemies import *

# The player will begin in the cell of the bandit hideout.
start_room = "kidnapped_cell"

# --- 1. Bandit Hideout (Tutorial Area) ---

room_kidnapped_cell = {
    "name": "Kidnapped Cell",
    "description":
    """You awaken on a cold stone floor, head throbbing.\nThe room is small and bare, save for a pile of straw and a heavy wooden door to the north.\nStill wondering how you got here you decide to investigate by trying to pry open the door.\nUse "go north" to move to the next room. """,
    "exits": {"north": "storage_room"},
    "enemy": None,
    "items": []
}

room_storage_room = {
    "name": "Dusty Storage Room",
    "description":
    """The door opens into a small storeroom filled with crates of stale rations and cheap ale.\nIt smells of damp earth.\nThere is a doorway leading east into what sounds like a larger common area.\nYou think you can hear someone moving around.\nMaybe its one of your captors?""",
    "exits": {"south": "kidnapped_cell", "east": "common_room"},
    "enemy": None,
    "items": [item_potion_health_small]
}

room_common_room = {
    "name": "Bandit Common Room",
    "description":
    """This is the bandits' main living space.\nA crude wooden table is surrounded by stools, and playing cards are scattered across its surface.\nA bored-looking bandit guard stands between you and a door to the north.\nTo the east is a heavy door that seems to lead outside.\nAs you take a step into the room the bandit runs at you!\nIts time to fight!\nUse "attack" to hit the enemy """,
    "exits": {"west": "storage_room", "north": "armory", "east": "hideout_exit"},
    "enemy": "bandit", #
    "items": []
}

room_armory = {
    "name": "Bandit Armory",
    "description":
    """This small room is cluttered with stolen goods.\nOn three crates in the center, three distinct sets of gear are displayed: the heavy plate of a FIGHTER, the swift leather of an ARCHER, and the enchanted robes of a MAGE.\nUse the "take" command to take your gear and start your adventure!""",
    "exits": {"south": "common_room"},
    "enemy": None,
    "items": [] #
}

room_hideout_exit = {
    "name": "Hideout Exit",
    "description":
    """You push the heavy door open and are greeted by the fresh, cold air of the mountains.\nYou've escaped the hideout.\nA narrow path leads north into the wilderness.""",
    "exits": {"west": "common_room", "north": "forest_clearing"},
    "enemy": None,
    "items": []
}

# --- 2. The Wilderness Hub ---

room_forest_clearing = {
    "name": "Forest Clearing",
    "description":
    """The path opens into a quiet clearing.\nA circle of mossy stones suggests this place was once sacred.\nNow, it feels eerie and abandoned.\nPaths lead west into a murky swamp, east towards a fortified castle, and north to the base of the Dragon's Peak.""",
    "exits": {"south": "hideout_exit", "west": "murky_swamp", "east": "knights_castle_drawbridge", "north": "dragon_peak_trail"},
    "enemy": None, # A safe zone hub.
    "items": [item_potion_mana_small]
}

# --- 3A. The Witch's Cabin (West Path) ---

room_murky_swamp = {
    "name": "Murky Swamp",
    "description":
    """The ground turns to mud and stagnant water.\nTwisted trees reach out like grasping claws, and the air is thick with the buzz of insects.\nA ghostly light flickers in the distance to the west.""",
    "exits": {"east": "forest_clearing", "west": "witchs_cabin"},
    "enemy": "ghost", #
    "items": []
}

room_witchs_cabin = {
    "name": "Witch's Cabin",
    "description":
    """A dilapidated cabin stands on stilts above the swamp water.\nInside, shelves are crammed with strange potions and arcane ingredients.\nA wizened witch cackles as you enter, her fingers crackling with dark energy.""",
    "exits": {"east": "murky_swamp"},
    "enemy": "witch", #
    "items": [item_spell_lightning] # The Witch's key and a spell reward.
}

# --- 3B. The Knight's Castle (East Path) ---

room_knights_castle_drawbridge = {
    "name": "Knight's Castle Drawbridge",
    "description":
    """A solid stone castle stands before you, its drawbridge lowered across a deep moat.\nThe banners hanging from its walls are tattered but noble.\nSkeletons of fallen soldiers patrol the entrance.""",
    "exits": {"west": "forest_clearing", "north": "castle_barracks"},
    "enemy": "skeleton", #
    "items": []
}

room_castle_barracks = {
    "name": "Castle Barracks",
    "description":
    """The barracks are orderly but empty.\nWeapon racks line the walls, and training dummies stand riddled with sword-cuts.\nA large door to the north leads to the throne room.""",
    "exits": {"south": "knights_castle_drawbridge", "north": "throne_room"},
    "enemy": None,
    "items": [item_armor_iron_set] #
}

room_throne_room = {
    "name": "Throne Room",
    "description":
    """This was once a grand throne room, but now it is a place of sorrow.\nA disgraced, Fallen Knight stands guard, his armor blackened by some terrible magic.\nHe raises his greatsword, honor-bound to defend this place to the death.""",
    "exits": {"south": "castle_barracks"},
    "enemy": "knight", #
    "items": [item_fighter_greatsword] # The Knight's key and a weapon reward.
}

# --- 4. The Dragon's Peak (Final Area) ---

room_dragon_peak_trail = {
    "name": "Dragon's Peak Trail",
    "description":
    """A steep, winding trail leads up the side of a soot-stained mountain.\nThe air grows warmer and carries the scent of brimstone.\nThe path is guarded by a massive stone golem, animated by the dragon's magic.""",
    "exits": {"south": "forest_clearing", "up": "great_hall"},
    "enemy": "stone_golem", #
    "items": []
}

room_great_hall = {
    "name": "The Great Hall",
    "description":
    """You enter the dragon's fortress.\nThis was once a magnificent hall, but now its banners are burned and the long tables are overturned.\nAt the far end, a massive, magically sealed door pulses with a faint light.\nIt seems to require two powerful artifacts to open.""",
    "exits": {"down": "dragon_peak_trail", "north": "dragon_lair"},
    "enemy": None,
    "items": []
}

room_dragon_lair = {
    "name": "Dragon's Lair",
    "description":
    """You open the door into a vast, cavernous chamber.\nThe roof has collapsed, revealing the stormy sky above.\nIn the center of the room, a colossal Ashen Dragon coils around a pile of treasure.\nCowering nearby is Princess Kirill!""",
    "exits": {"south": "great_hall"},
    "enemy": "dragon", #
    "items": []
}

# --- Master Room Registry ---
rooms = {
    "kidnapped_cell": room_kidnapped_cell,
    "storage_room": room_storage_room,
    "common_room": room_common_room,
    "armory": room_armory,
    "hideout_exit": room_hideout_exit,
    "forest_clearing": room_forest_clearing,
    "murky_swamp": room_murky_swamp,
    "witches_cabin": room_witchs_cabin,
    "knights_castle_drawbridge": room_knights_castle_drawbridge,
    "castle_barracks": room_castle_barracks,
    "throne_room": room_throne_room,
    "dragon_peak_trail": room_dragon_peak_trail,
    "great_hall": room_great_hall,
    "dragon_lair": room_dragon_lair
}
