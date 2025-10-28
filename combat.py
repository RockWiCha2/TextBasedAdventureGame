from classes import *
from items import *
from gameParser import *
from enemies import *
from dungeon_map import *
import random

import gui


def render_combat_screen(player, monster, extra_lines=None):
    """Renders the combat UI, now with dynamic options."""
    if extra_lines is None:
        extra_lines = []

    #Renders the details of the enemy
    enemy_name = monster.get("name", "Enemy")
    enemy_desc = monster.get("description", "")
    enemy_hp = monster.get("health", "?")

    #Renders the player details
    player_hp = player.get("health", 0)
    player_mana = player.get("mana", None)
    dmg_mult = player.get("damageMult", 1)

    hp_line = f"Your HP: {player_hp}" + (f"   |   Mana: {player_mana}" if player_mana is not None else "")
    vs_line = f"{enemy_name} HP: {enemy_hp}"
    stats_line = f"Your DMG x{dmg_mult}"

    #Shows the player the options for which actions they can take
    options = ["|| ATTACK ||", "|| DEFEND ||", "|| USE <item> ||"]
    if player.get("name") == "mage":  #
        options.append("|| CAST <spell> ||")  # Add cast option only for mages
    options.append("|| FLEE ||")
    options_str = "  ".join(options)

    combined = (
            f"<b>{enemy_name}</b>\n"
            f"<i>{enemy_desc}</i>\n\n"
            f"{hp_line}\n{vs_line}\n{stats_line}\n\n"
            + ("\n".join(extra_lines) + ("\n\n" if extra_lines else ""))
            + "<b>Choose an action:</b>\n"
            + options_str
    )
    gui.gui_print(combined)


def find_item_in_inventory(item_name_to_find):
    #Searches the items in the inventory and adds it to a list to be used
    found_items = []
    for item in inventory:
        if item_name_to_find.lower() in item["name"].lower():
            found_items.append(item)
    return found_items


def find_quiver_in_inventory():
    for item in inventory:
        if item.get("ammo_type") == "arrow":
            return item
    return None


def get_current_weapon(inventory):
    #Looks for a weapon in the inventory
    for i in inventory:
        if i["type"] == "weapon":
            return i
    return fist_attack  # Default to fists if no weapon


def get_current_armor(inventory):
    #Looks for armour in the inventory
    for i in inventory:
        if i["type"] == "armor":
            return i
    return {"block": 0}  # Default to 0 block if no armor


def start_encounter(player, monster_key):
    monster = enemies[monster_key].copy()  # Creating a fresh copy to avoid changing the master template

    # Setting the base states for each variable
    monster_alive = True
    player_alive = True
    player_defending = False

    #Calling the searches for weapon and armour
    currentWeapon = get_current_weapon(inventory)
    currentArmor = get_current_armor(inventory)

    # Finding players current stats
    player_health = player["health"]
    player_mana = player.get("mana", 0)

    turn_messages = []

    while monster_alive and player_alive:
        player["health"] = player_health
        if "mana" in player:
            player["mana"] = player_mana

        render_combat_screen(player, monster, extra_lines=turn_messages)
        turn_messages = []

        # Asks the user what they want to do
        raw_input_text = gui.get_text_input()
        userinput = normalise_input(raw_input_text)
        monster_turn = True

        if not userinput:
            turn_messages.append("You hesitate, unsure of what to do.")
            monster_turn = False
            continue

        command = userinput[0]

        # Handles the melee / ranged attack
        if command == "attack":
            # Checks to see if the player is an archer
            if player["name"] == "archer":  #
                quiver = find_quiver_in_inventory()
                # Finds the quiver, takes a shot and reduces the amount of ammo in the quiver
                if quiver and quiver.get("ammo", 0) > 0:
                    quiver["ammo"] -= 1
                    turn_messages.append(f"You fire an arrow from your {currentWeapon['name']}!")
                    totalDamage = player["damageMult"] * currentWeapon["damage"]
                    if totalDamage < 0: totalDamage = 0
                    turn_messages.append(f"You hit {monster['name']} with {totalDamage} damage.")
                    turn_messages.append(f"(You have {quiver['ammo']} arrows left.)")
                    monster["health"] -= totalDamage
                else:
                    # If the quiver is empty, resort to a melee attack
                    turn_messages.append("You're out of arrows! You bash the enemy with your bow.")
                    monster["health"] -= 2
            else:
                if player["name"] == "mage":  #
                    turn_messages.append("You swing your staff...")
                    totalDamage = currentWeapon["damage"]
                else:
                    #Handles the melee attacks for fighters
                    turn_messages.append(f"You swing your {currentWeapon['name']}!")
                    totalDamage = player["damageMult"] * currentWeapon["damage"]
                if totalDamage < 0: totalDamage = 0
                turn_messages.append(f"You hit {monster['name']} with {totalDamage} damage.")
                monster["health"] -= totalDamage

            turn_messages.append(f"The {monster['name']} now has {monster['health']} health.")

        # Handles the casting of spells
        elif command == "cast":
            if player["name"] != "mage":  #
                turn_messages.append("You don't know how to cast spells!")
                monster_turn = False
            elif len(userinput) > 1:
                spell_name_to_cast = " ".join(userinput[1:])
                spell = find_item_in_inventory(spell_name_to_cast)
                if spell and spell[0].get("type") == "spell":
                    spell_item = spell[0]
                    mana_cost = spell_item.get("mana_cost", 0)
                    if player_mana >= mana_cost:
                        player_mana -= mana_cost
                        spell_damage = spell_item.get("damage", 0)
                        spell_power_bonus = currentWeapon.get("spell_power", 0)
                        total_spell_damage = spell_damage + spell_power_bonus
                        turn_messages.append(f"You cast {spell_item['name']} for {total_spell_damage} damage!")
                        monster["health"] -= total_spell_damage  # FIX: Damage the local monster copy
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

        # Allows the user to use items such as health and mana potions
        elif command == "use":
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
                        if player_health > player["health"]: player_health = player["health"]
                        inventory.remove(item)
                        turn_messages.append(
                            f"You use {item['name']} and restore {restore_amount} health. You now have {player_health} HP.")
                    else:
                        turn_messages.append(f"You can't use the {item['name']} right now.")
                else:
                    turn_messages.append("Which item did you mean? Be more specific.")
                    for item in matched_items: turn_messages.append(f"- {item['name']}")
                    monster_turn = False
            else:
                turn_messages.append("Use what? (e.g., 'use small health potion')")
                monster_turn = False

        elif command == "flee":
            player_speed = 5
            monster_speed = monster.get("speed", 1)  # Not all enemies have speed, so default to 1
            flee_chance = random.randint(1, player_speed + monster_speed)
            if flee_chance > monster_speed:
                render_combat_screen(player, monster,
                                     extra_lines=[f"You successfully escape from the {monster['name']}!"])
                gui.get_text_input()
                return
            else:
                turn_messages.append(f"You try to run, but the {monster['name']} is too fast!")
        else:
            turn_messages.append("You hesitate, unsure of what to do.")
            monster_turn = False

        if monster["health"] <= 0:
            render_combat_screen(player, monster, extra_lines=[f"<b>You have defeated the {monster['name']}!</b>"])
            gui.get_text_input()
            monster_alive = False
            break

        if monster_turn:
            turn_messages.append(f"The {monster['name']} attacks you!")
            # --- FIX: Use helper function to get armor block ---
            player_block = currentArmor.get("block", 0)
            if player_defending:
                player_block *= 2
                turn_messages.append("Your defensive stance softens the blow!")
                player_defending = False

            monster_damage = roll_damage(monster) - player_block
            if monster_damage < 0: monster_damage = 0

            player_health -= monster_damage
            turn_messages.append(
                f"You were hit for {monster_damage} damage. You have {player_health} health remaining.")

            if player_health <= 0:
                player_alive = False

    if not player_alive:
        render_combat_screen(player, monster, extra_lines=["<b>You have been defeated. Game Over.</b>"])
        gui.get_text_input()
        # Here you would typically exit the game or load a save