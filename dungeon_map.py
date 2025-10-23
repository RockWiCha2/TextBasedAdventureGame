start_room = "sealed_gate"

room_sealed_gate = {
    "name": "Sealed Gate",
    "description":
    """A stone arch blocks the way with a slab etched in worn runes. A tiny draft
whistles through hairline cracks, carrying the smell of old dust. A tarnished
ring of keys hangs from a nail, all of them the wrong shape for this door.
Scratches on the floor suggest the slab once slid aside. A rough passage runs
north, and a low crawlspace continues east.""",
    "exits": {"north": "ladder_shaft", "east": "fungal_niche"}
}

room_ladder_shaft = {
    "name": "Ladder Shaft",
    "description":
    """An open shaft yawns above, its rungs warped and slick with age. You can make
out a faint rectangle of light far overhead, well beyond reach. Someone has
chiseled tally marks into the wall at shoulder height. A coil of rotten rope
lies in a heap, better left untouched. Passages run north, east, and south.""",
    "exits": {"north": "collapsed_corridor", "east": "scribe_cell", "south": "sealed_gate"}
}

room_collapsed_corridor = {
    "name": "Collapsed Corridor",
    "description":
    """Most of the ceiling has given way here, forming an ankle-twisting ridge of
rubble. A draft hisses through gaps between stones, making a sound like distant
whispers. Faded arrows painted on the wall point in several directions, none
particularly trustworthy. A battered lantern hook suggests this was once busy.
Exits lead north, east, and south.""",
    "exits": {"north": "watch_post", "east": "antechamber", "south": "ladder_shaft"}
}

room_watch_post = {
    "name": "Watch Post",
    "description":
    """A narrow alcove overlooks the corridor through a murder slit. A stool rests
on three legs, the fourth carefully carved into a makeshift wedge nearby.
Old dice lie in a shallow bowl, all showing different numbers of pips than they
should. The room is quiet, and the slit admits only a stripe of chill air.
You can go east or south from here.""",
    "exits": {"east": "guardroom", "south": "collapsed_corridor"}
}

room_guardroom = {
    "name": "Guardroom",
    "description":
    """Hooks line the walls where helmets once hung in tidy rows. A chalk board
lists shifts in a hand that gets steadily sloppier near the end. The remains of
a card game are scattered on a barrel-top, one card burned around its edges.
A dented gong hangs from a beam, mercifully silent. Doorways open west, east,
and south.""",
    "exits": {"west": "watch_post", "east": "armory", "south": "antechamber"}
}

room_armory = {
    "name": "Armory",
    "description":
    """Empty racks stand like ribs, their pegs stained with dark oil. A few blunt
practice blades lie underfoot, more hazard than help. Someone has carved a
simple map into a beam, but half of it has flaked away. A crate rattles when
nudged, though nothing comes out. You can head west or south.""",
    "exits": {"west": "guardroom", "south": "cistern"}
}

room_antechamber = {
    "name": "Antechamber",
    "description":
    """A modest hall with sagging banners and a cracked floor mosaic. Footprints
overlap in dusty loops as if patrols once circled here endlessly. A niche holds
a chipped basin, dry for years. The air tastes faintly metallic, like old keys.
Corridors lead north, east, south, and west.""",
    "exits": {"north": "guardroom", "east": "cistern", "south": "scribe_cell", "west": "collapsed_corridor"}
}

room_cistern = {
    "name": "Cistern",
    "description":
    """A stone pool sits in the center, its water long since evaporated to a ring
of white crust. A bucket on a chain hangs just above the basin, immovable.
Drips tick somewhere out of sight, maddeningly irregular. Moss clings to the
lower stones where the light never reaches. Exits go north, west, and south.""",
    "exits": {"north": "armory", "west": "antechamber", "south": "crypt"}
}

room_scribe_cell = {
    "name": "Scribe Cell",
    "description":
    """A cramped cell with a slanted desk and a sand tray for blotting. Notes about
door levers, lantern hooks, and tally marks are scattered like fallen leaves.
The ink is dry and dusty, yet your fingertips come away faintly smudged.
A tiny shelf holds a blank seal and a broken quill. You can go north, east,
south, or west.""",
    "exits": {"north": "antechamber", "east": "crypt", "south": "fungal_niche", "west": "ladder_shaft"}
}

room_crypt = {
    "name": "Crypt",
    "description":
    """Recesses in the walls hold nameless stone lids, all identical. The floor is
smoother here, as if many careful steps wore it down over years. A draft slips
through the seams and brings a smell like old paper. A single candle stub rests
in a niche, eternally unlit. Passages lead north, west, and south.""",
    "exits": {"north": "cistern", "west": "scribe_cell", "south": "treasury"}
}

room_fungal_niche = {
    "name": "Fungal Niche",
    "description":
    """Pale caps crowd the corners, spreading in perfect circles around old drips.
A few are bruised where someone tested their texture and thought better of it.
Your footsteps are quiet here, swallowed by soft growth. The ceiling dips low,
forcing a slight stoop. Ways lead north, east, and west.""",
    "exits": {"north": "scribe_cell", "east": "treasury", "west": "sealed_gate"}
}

room_treasury = {
    "name": "Treasury",
    "description":
    """Iron-banded chests line the walls, most pried open and disappointingly empty.
A ledger lies on a stand, every value neatly recorded and then crossed out.
One chest’s hinge squeals when touched, loud enough to feel unwise. Dust motes
turn in the thin light from a high grate. Exits are to the north and west.""",
    "exits": {"north": "crypt", "west": "fungal_niche"}
}

# --- Master room registry using themed lowercase_underscore keys ---
rooms = {
    "sealed_gate": room_sealed_gate,
    "ladder_shaft": room_ladder_shaft,
    "collapsed_corridor": room_collapsed_corridor,
    "watch_post": room_watch_post,
    "guardroom": room_guardroom,
    "armory": room_armory,
    "antechamber": room_antechamber,
    "cistern": room_cistern,
    "scribe_cell": room_scribe_cell,
    "crypt": room_crypt,
    "fungal_niche": room_fungal_niche,
    "treasury": room_treasury,
}
