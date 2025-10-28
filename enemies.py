import random

def roll_damage(enemy_dict):

    low, high = enemy_dict.get("damage_range", (1, 1))
    return random.randint(1, high)

enemy_bandit = {
    "id": "bandit",
    "name": "Bandit",
    "description": "A jittery roadside cutpurse with more nerves than skill.",
    "health": 18,
    "damage_range": (5, 7),
    "is_boss": False
}

enemy_skeleton = {
    "id": "skeleton",
    "name": "Skeleton",
    "description": "Castle guard bones wired together by stale sorcery.",
    "health": 26,
    "damage_range": (5, 10),
    "is_boss": False
}

enemy_ghost = {
    "id": "ghost",
    "name": "Ghost",
    "description": "A pale silhouette drifting between torn banners.",
    "health": 24,
    "damage_range": (5, 10),
    "is_boss": False
}

enemy_knight = {
    "id": "knight",
    "name": "Fallen Knight",
    "description": "A once-honorable champion sealed inside blackened plate.",
    "health": 60,
    "damage_range": (20, 30),
    "is_boss": True
}

enemy_giant_bat = {
    "id": "giant_bat",
    "name": "Giant Bat",
    "description": "A ceiling-spanning nightmare with leather wings and needle fangs.",
    "health": 32,
    "damage_range": (15, 17),
    "is_boss": False
}

enemy_witch = {
    "id": "witch",
    "name": "Witch",
    "description": "A scholar of bitter moons, draped in raven thread.",
    "health": 54,
    "damage_range": (20, 30),
    "is_boss": True
}

enemy_stone_golem = {
    "id": "stone_golem",
    "name": "Stone Golem",
    "description": "A walking bulwark carved from the castle’s own foundations.",
    "health": 80,
    "damage_range": (30, 40),
    "is_boss": False
}

enemy_dragon = {
    "id": "dragon",
    "name": "Ashen Dragon",
    "description": "The crown of calamities coils atop the highest spire.",
    "health": 220,
    "damage_range": (50, 60),
    "is_boss": True
}

# --- Master Enemy Registry ---
# This dictionary maps the string ID (used in your map file) to the full enemy dictionary.
enemies = {
    "bandit": enemy_bandit,
    "skeleton": enemy_skeleton,
    "ghost": enemy_ghost,
    "knight": enemy_knight,
    "giant_bat": enemy_giant_bat,
    "witch": enemy_witch,
    "stone_golem": enemy_stone_golem,
    "dragon": enemy_dragon
}
