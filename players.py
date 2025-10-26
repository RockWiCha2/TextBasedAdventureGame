class Player:
    def __init__(self, name, player_class):
        self.name = name        #sets the players name
        self.player_class = player_class  #sets the class
        
      
        base_stats = self.set_base_stats(player_class)      #depends on the class
        self.health = base_stats['health']      #health points
        self.mana = base_stats['mana']
        self.damage = base_stats['damage']
        self.armour = base_stats['armour']
        
        self.inventory = []  # allows player to have an inventory
        self.equipment = {      #what the player currently has equipped
            'weapon': None,
            'armor': None,
            'accessory': None
        }

    def set_base_stats(self, player_class):     #sets the starting stats based on the players base class
        classes = {
            "Fighter": {"health": 150, "mana": 30, "damage": 15, "armour": 10},
            "Mage":    {"health": 80, "mana": 120, "damage": 25, "armour": 3},
            "Archer":   {"health": 100, "mana": 50, "damage": 20, "armour": 5},
            
        }
        return classes.get(player_class, {"health": 100, "mana": 50, "damage": 10, "armour": 5})    #returns matching stats or default if unknown

    def take_damage(self, amount):
        reduced_amount = max(0, amount - self.armour)   #calculates the damage taken after armour applied
        self.health -= reduced_amount #takes reduced damage from players health
        print(f"{self.name} takes {reduced_amount} damage! Health is now {self.health}.")   #diplays new hjealth value
        if self.health <= 0:        #if health less then zero player died
            print(f"{self.name} has fallen!")

    def use_mana(self, amount):#checks if player has enough mana to perform action
        if self.mana >= amount: #deducts mana
            self.mana -= amount
            print(f"{self.name} uses {amount} mana. Remaining mana: {self.mana}")
            return True
        else:   #not enough mana to perform action
            print(f"Not enough mana! {self.name} has only {self.mana} mana.")
            return False

    def add_to_inventory(self, item):
        self.inventory.append(item) # adds new iyem to inventory list
        print(f"{item} added to inventory.")    #confirms

    def equip_item(self, slot, item):
        if slot in self.equipment:  #checks if provided item is valid
            self.equipment[slot] = item
            print(f"{self.name} equips {item} in slot {slot}.")
        else:   #invalid slot name
            print(f"Invalid equipment slot: {slot}")

    def show_status(self):  #diplays status of the player in clear format
        print(f"--- {self.name}'s Status ---")  
        print(f"Class: {self.player_class}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        print(f"Damage: {self.damage}")
        print(f"Armour: {self.armour}")
        print(f"Inventory: {self.inventory}")
        print(f"Equipment: {self.equipment}")
        print("------------------------")


