from players import *
from classes import *
from items import *
from gameParser import *
from enemies import *
from dungeon_map import *
import random

import gui

temp_bat = {
    "id": "bat_id",
    "name": "Bat",
    "description": "",
    "damage": 20,
    "health": 100,
    "block": 5,
    "speed": 10
}

temp_warrior = {
    "id": "warrior",
    "name": "Harri",
    "strength": 10,
    "health": 100,
    "weapon": item_fighter_greatsword,
    "shield": item_shield_iron,
    "armour": item_armor_iron_set
}

def render_combat_screen(player, monster_key, extra_lines=None):
    """
    Combine combat info and options into ONE gui.gui_print() call (menu-style).
    monster_key is the key used to index into the global enemies dict.
    extra_lines: list[str] of outcome messages to show this turn.
    """
    if extra_lines is None:
        extra_lines = []

    enemy = enemies[monster_key]
    enemy_name = enemy.get("name", "Enemy")
    enemy_desc = enemy.get("description", "")
    enemy_hp = enemy.get("health", "?")

    player_hp = player.get("health", 0)
    player_mana = player.get("mana", None)
    dmg_mult = player.get("damageMult", 1)

    hp_line = f"Your HP: {player_hp}" + (f"   |   Mana: {player_mana}" if player_mana is not None else "")
    vs_line = f"{enemy_name} HP: {enemy_hp}"
    stats_line = f"Your DMG x{dmg_mult}"

    options = "|| ATTACK ||  || DEFEND ||  || USE <item> ||  || FLEE ||"

    combined = (
        f"{enemy_name}\n"
        f"{enemy_desc}\n\n"
        f"{hp_line}\n{vs_line}\n{stats_line}\n\n"
        + ("\n".join(extra_lines) + ("\n\n" if extra_lines else ""))
        + "Choose an action:\n"
        + options
    )
    gui.gui_print(combined)
def get_weapon(inventory):
    currentweapon = fist_attack
    for i in inventory:
            if i["type"]=="weapon":
                currentWeapon = i
            
    return currentWeapon
def find_item_in_inventory(item_name_to_find):
    found_items = []
    for item in inventory: #
        if item_name_to_find.lower() in item["name"].lower(): #
            found_items.append(item) #
    return found_items #

def find_quiver_in_inventory():
    for item in inventory:
        if item.get("ammo_type") == "arrow":
            return item
    return None

def get_current_weapon(inventory):
    currentWeapon = fist_attack
    for i in inventory:
            if i["type"]=="weapon":
                currentWeapon = i
            print(currentWeapon, i)
    return currentWeapon
        
def start_encounter(player, monster):
    # State flags
    monster_alive = True
    player_alive = True
    player_defending = False

    # Determine current weapon from inventory (keep existing helper)
    currentWeapon = get_current_weapon(inventory)

    # Local live stats
    player_health = player["health"]
    player_mana = player.get("mana", None)

    # Buffer for outcome messages displayed on the next screen
    turn_messages = []

    while monster_alive and player_alive:
        # Sync live values back for display
        player["health"] = player_health
        if player_mana is not None:
            player["mana"] = player_mana

        # Render one combined combat screen (like menu)
        render_combat_screen(player, monster, extra_lines=turn_messages)
        turn_messages = []  # reset buffer for this turn

        # Get command via GUI (non-blocking for window)
        raw_input_text = gui.get_text_input()
        userinput = normalise_input(raw_input_text)
        monster_turn = True

        # Check for empty input after normalization
        if not userinput:
            turn_messages.append("You hesitate, unsure of what to do.")
            monster_turn = False
            continue

        command = userinput[0]

        if command == "attack":
            # Archer Attack Logic
            if player == "archer":
                quiver = find_quiver_in_inventory()
                if quiver and quiver.get("ammo", 0) > 0:
                    quiver["ammo"] -= 1  # Deplete one arrow
                    turn_messages.append(f"You fire an arrow from your {currentWeapon['name']}!")
                    totalDamage = player["damageMult"] * currentWeapon["damage"]
                    if totalDamage < 0:
                        totalDamage = 0
                    turn_messages.append(f"You hit {enemies[monster]['name']} with {totalDamage} damage.")
                    turn_messages.append(f"(You have {quiver['ammo']} arrows left.)")
                    enemies[monster]["health"] -= totalDamage
                else:
                    turn_messages.append("You're out of arrows! You bash the enemy with your bow.")
                    totalDamage = 2
                    turn_messages.append(f"You hit {enemies[monster]['name']} with {totalDamage} damage.")
                    enemies[monster]["health"] -= totalDamage
            # Fighter / Mage Melee Logic
            else:
                if player == "mage":
                    turn_messages.append("You swing your staff...")
                    totalDamage = currentWeapon["damage"]
                else:
                    turn_messages.append(f"You swing your {currentWeapon['name']}")
                    totalDamage = player["damageMult"] * currentWeapon["damage"]
                if totalDamage < 0:
                    totalDamage = 0
                turn_messages.append(f"You hit {enemies[monster]['name']} with {totalDamage} damage.")
                enemies[monster]["health"] -= totalDamage

            turn_messages.append(f"The {enemies[monster]['name']} now has {enemies[monster]['health']} health.")

        elif command == "cast":
            if player["class"]["name"] != "mage":
                turn_messages.append("You don't know how to cast spells!")
                monster_turn = False
            elif len(userinput) > 1:
                spell_name_to_cast = " ".join(userinput[1:])
                spell = find_item_in_inventory(spell_name_to_cast)
                if spell and spell[0].get("type") == "spell":
                    spell_item = spell[0]
                    mana_cost = spell_item.get("mana_cost", 0)
                    if (player_mana or 0) >= mana_cost:
                        player_mana = (player_mana or 0) - mana_cost
                        spell_damage = spell_item.get("damage", 0)
                        spell_power_bonus = player["weapon"].get("spell_power", 0)
                        total_spell_damage = spell_damage + spell_power_bonus
                        turn_messages.append(f"You cast {spell_item['name']} for {total_spell_damage} damage!")
                        enemies[monster]["health"] -= total_spell_damage
                    else:
                        turn_messages.append("You don't have enough mana to cast that spell!")
                        monster_turn = False
                else:
                    turn_messages.append("You don't know that spell.")
                    monster_turn = False
            else:
                turn_messages.append("Cast what spell?")
                monster_turn = False

        elif command == "defend":
            player_defending = True
            turn_messages.append("You raise your shield and brace for attack!")

        elif command == "use":  # Using 'command' variable
            if len(userinput) > 1:
                item_name_to_use = " ".join(userinput[1:])
                matched_items = find_item_in_inventory(item_name_to_use)
                if not matched_items:
                    turn_messages.append("You don't have that item in your inventory.")
                    monster_turn = False
                elif len(matched_items) == 1:
                    item = matched_items[0]
                    if item.get("type") == "health_potion":
                        restore_amount = item.get("restore_hp", 0)
                        player_health += restore_amount
                        if player_health > player["class"]["health"]:
                            player_health = player["class"]["health"]
                        inventory.remove(item)
                        turn_messages.append(f"You use {item['name']} and restore {restore_amount} health. You now have {player_health} HP.")
                    else:
                        turn_messages.append(f"You can't use the {item['name']} right now.")
                else:
                    turn_messages.append("Which item did you mean? Be more specific.")
                    for item in matched_items:
                        turn_messages.append(f"- {item['name']}")
                    monster_turn = False
            else:
                turn_messages.append("Use what? (e.g., 'use small health potion')")
                monster_turn = False

        elif command == "flee":
            player_speed = 5
            monster_speed = enemies[monster].get("speed", 1)
            flee_chance = random.randint(1, player_speed + monster_speed)
            if flee_chance > monster_speed:
                render_combat_screen(player, monster, extra_lines=[f"You successfully escape from the {enemies[monster]['name']}!"])
                gui.get_text_input()
                return
            else:
                turn_messages.append(f"You try to run, but the {enemies[monster]['name']} is too fast!")
        else:
            turn_messages.append("You hesitate, unsure of what to do.")
            monster_turn = False

        # Victory check mid-turn
        if enemies[monster]["health"] <= 0:
            render_combat_screen(player, monster, extra_lines=[f"You have defeated the {enemies[monster]['name']}!"])
            gui.get_text_input()
            monster_alive = False
            monster_turn = False
            break

        # Monster's turn
        if monster_turn:
            turn_messages.append(f"The {enemies[monster]['name']} attacks you!")
            player_block = currentArmor["block"]
            if player_defending:
                player_block *= 2
                turn_messages.append("Your defensive stance softens the blow!")
                player_defending = False

            monster_damage = roll_damage(enemies[monster]) - player_block
            if monster_damage < 0:
                monster_damage = 0

            player_health -= monster_damage
            turn_messages.append(f"You were hit for {monster_damage} damage. You have {player_health} health remaining.")

            if player_health <= 0:
                player_alive = False
                break

    # After the loop, check the result (convert to GUI)
    if player_health <= 0:
        render_combat_screen(player, monster, extra_lines=["You have been defeated. Game Over."])
        gui.get_text_input()
