from players import *
from classes import *
from items import *
from gameParser import *
from enemies import *
from dungeon_map import *
import random

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
    monster_alive = True
    player_alive = True
    player_defending = False
    currentWeapon = get_current_weapon(inventory)
    print(currentWeapon)
    player_health = player["health"]
    player_mana = player["mana"]
    if player== "mage":  #
        print(f"HP: {player_health} | Mana: {player_mana}")
    else:
        print(f"HP: {player_health}")

    '''print(f"A terrifying", {monster["name"]} ,"appears!")'''
    while monster_alive and player_alive:
        print("What do you want to do? (Attack, Defend, Use or Flee)")
        raw_input = input("> ")
        userinput = normalise_input(raw_input)
        monster_turn = True
    
        # Check for empty input after normalization
        if not userinput:
            print("You hesitate, unsure of what to do.")
            monster_turn = False
            continue

        command = userinput[0]
        
        if command == "attack":
            if command == "attack":
                # --- Archer Attack Logic ---
                if player == "archer":  #
                    quiver = find_quiver_in_inventory()

                    if quiver and quiver.get("ammo", 0) > 0:
                        quiver["ammo"] -= 1  # Deplete one arrow

                        print(f"You fire an arrow from your {currentWeapon['name']}!")
                        totalDamage = player["damageMult"] * currentWeapon["damage"]  #
                        if totalDamage < 0: totalDamage = 0

                        print(f"You hit {monster['name']} with {totalDamage} damage.")  #
                        print(f"(You have {quiver['ammo']} arrows left.)")
                        enemies[monster]["health"] -= totalDamage  #
                    else:
                        print("You're out of arrows! You bash the enemy with your bow.")
                        totalDamage = 2
                        print("You hit", monster,"with",totalDamage,"damage.")  #
                        enemies[monster]["health"] -= totalDamage  #

                # --- Fighter / Mage Melee Logic ---
                else:
                    if player == "mage":  #
                        print("You swing your staff...")
                        totalDamage = currentWeapon["damage"]
                    else:
                        print(f"You swing your", currentWeapon["name"])
                        totalDamage = player["damageMult"] * currentWeapon["damage"]#

                    if totalDamage < 0: totalDamage = 0

                    print("You hit", monster,"with",totalDamage,"damage.")  #
                    enemies[monster]["health"] -= totalDamage  #

                print("The", monster,"now has",enemies[monster]["health"],"health.")  #

        elif command == "cast":
            if player["class"]["name"] != "mage":  #
                print("You don't know how to cast spells!")
                monster_turn = False
            elif len(userinput) > 1:
                spell_name_to_cast = " ".join(userinput[1:])
                spell = find_item_in_inventory(spell_name_to_cast)

                if spell and spell[0].get("type") == "spell":
                    spell_item = spell[0]
                    mana_cost = spell_item.get("mana_cost", 0)  #

                    if player_mana >= mana_cost:
                        player_mana -= mana_cost
                        spell_damage = spell_item.get("damage", 0)  #
                        spell_power_bonus = player["weapon"].get("spell_power", 0)  #
                        total_spell_damage = spell_damage + spell_power_bonus

                        print(f"You cast {spell_item['name']} for {total_spell_damage} damage!")
                        monster["health"] -= total_spell_damage
                    else:
                        print("You don't have enough mana to cast that spell!")
                        monster_turn = False
                else:
                    print("You don't know that spell.")
                    monster_turn = False
            else:
                print("Cast what spell?")
                monster_turn = False

        elif command == "defend":
            player_defending = True
            print("You raise your shield and brace for attack!")

        elif command == "use": # FIX: Using 'command' variable
            if len(userinput) > 1: # FIX: Using 'userinput' list
                item_name_to_use = " ".join(userinput[1:]) # FIX: Using 'userinput' list
                matched_items = find_item_in_inventory(item_name_to_use)

                if not matched_items:
                    print("You don't have that item in your inventory.")
                    monster_turn = False
                elif len(matched_items) == 1:
                    item = matched_items[0]
                    if item.get("type") == "health_potion":
                        restore_amount = item.get("restore_hp", 0)
                        player_health += restore_amount
                        if player_health > player["class"]["health"]:
                            player_health = player["class"]["health"]
                        inventory.remove(item)
                        print(f"You use {item['name']} and restore {restore_amount} health. You now have {player_health} HP.")
                    else:
                        print(f"You can't use the {item['name']} right now.")
                else:
                    print("Which item did you mean? Be more specific.")
                    for item in matched_items:
                        print(f"- {item['name']}")
                    monster_turn = False
            else:
                print("Use what? (e.g., 'use small health potion')")
                monster_turn = False

        elif command == "flee":
            player_speed = 5
            monster_speed = monster.get("speed", 1)
            flee_chance = random.randint(1, player_speed + monster_speed)
            if flee_chance > monster_speed:
                print(f"You successfully escape from the {monster['name']}!")
                return
            else:
                print(f"You try to run, but the {monster['name']} is too fast!")
        else:
            print("You hesitate, unsure of what to do.")
            monster_turn = False

        if enemies[monster]["health"] <= 0:
            print("You have defeated the", enemies[monster]["name"],"!")
            monster_alive = False
            monster_turn = False
        if monster_turn:
            print("The" ,enemies[monster]["name"]," attacks you!")
            player_block = currentArmor["block"]
            if player_defending:
                player_block *= 2
                print("Your defensive stance softens the blow!")
                player_defending = False

            monster_damage = roll_damage(enemies[monster]) - player_block
            if monster_damage < 0: monster_damage = 0

            player_health -= monster_damage
            print(f"You were hit for {monster_damage} damage. You have {player_health} health remaining.")

            if player_health <= 0: 
                player_alive = False

    # After the loop, check the result
    if player_health <= 0:
        print("\nYou have been defeated. Game Over.")
