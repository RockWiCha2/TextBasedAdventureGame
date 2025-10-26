from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Tuple
import random

@dataclass
class Enemy:
    id: str
    name: str
    description: str
    health: int
    damage_range: Tuple[int, int]
    is_boss: bool = False

    def roll_damage(self) -> int:
        """
        Roll damage as a random integer between damage_range[0] and damage_range[1] (inclusive).
        """
        low, high = self.damage_range
        return random.randint(low, high)


ENEMIES: Dict[str, Enemy] = {
    # 1) Bandit 
    "bandit": Enemy(
        id="bandit",
        name="Bandit",
        description=(
            "A jittery roadside cutpurse with more nerves than skill. His leather jerkin is scuffed, "
            "and his dagger hand shakes just a little. He talks a big game, but every feint is telegraphed "
            "a heartbeat too early. A perfect warm‑up for real danger."
        ),
        health=18,
        damage_range=(1, 3),
        is_boss=False,
    ),

    # 2) Skeleton 
    "skeleton": Enemy(
        id="skeleton",
        name="Skeleton",
        description=(
            "Castle guard bones wired together by stale sorcery. The jaw clacks as if trying to remember a war cry. "
            "Light and quick, it jabs with a rust‑pitted short sword and collapses into a clatter when struck smartly."
        ),
        health=26,
        damage_range=(2, 5),
        is_boss=False,
    ),

    # 3) Ghost 
    "ghost": Enemy(
        id="ghost",
        name="Ghost",
        description=(
            "A pale silhouette drifting between torn banners. Steel passes through like mist, but cold fingers "
            "can still rake the soul. It whispers fragments of old vows that make the air bite."
        ),
        health=24,
        damage_range=(3, 6),
        is_boss=False,
    ),

    # 4) Knight 
    "knight": Enemy(
        id="knight",
        name="Fallen Knight",
        description=(
            "A once‑honorable champion sealed inside blackened plate. Every step is a thud of iron and regret. "
            "A tower shield chewed by teeth marks blocks the obvious blows; only patience and timing slip past the rim."
        ),
        health=60,
        damage_range=(5, 10),
        is_boss=True,
    ),

    # 5) Giant Bat 
    "giant_bat": Enemy(
        id="giant_bat",
        name="Giant Bat",
        description=(
            "A ceiling‑spanning nightmare with leather wings and needle fangs. It dives in bursts, "
            "screeching so sharply your vision buzzes, then skitters away to turn and strike again."
        ),
        health=32,
        damage_range=(4, 8),
        is_boss=False,
    ),

    # 6) Witch 
    "witch": Enemy(
        id="witch",
        name="Witch",
        description=(
            "A scholar of bitter moons, draped in raven thread. Sigils flicker at her fingertips, and the air "
            "warps with each hissed syllable. She lashes hexes that sap strength and will, laughing softly when you miss."
        ),
        health=54,
        damage_range=(6, 12),
        is_boss=True,
    ),

    # 7) Stone Golem 
    "stone_golem": Enemy(
        id="stone_golem",
        name="Stone Golem",
        description=(
            "A walking bulwark carved from the castle’s own foundations. Moss binds the slabs; a dull ember glows deep inside. "
            "Slow, implacable, and almost deaf to pain, it smashes with a weight that rattles teeth."
        ),
        health=80,
        damage_range=(7, 13),
        is_boss=False,
    ),

    # 8) Dragon 
    "dragon": Enemy(
        id="dragon",
        name="Ashen Dragon",
        description=(
            "The crown of calamities coils atop the highest spire. Scales like kiln‑baked obsidian, eyes like banked furnaces. "
            "Wings beat storms into the courtyard. Its breath blooms into a white‑hot cone that turns banners to drifting ash."
        ),
        health=220,
        damage_range=(12, 20),
        is_boss=True,
    ),
}


def get_enemy(enemy_id: str) -> Enemy:
    """Fetch an enemy by its id. Raises KeyError if not found."""
    return ENEMIES[enemy_id]


def list_enemies() -> Dict[str, Enemy]:
    """Return the enemy registry (copy)."""
    return dict(ENEMIES)
