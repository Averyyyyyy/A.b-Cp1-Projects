 #Avery Mystery Arena: path to victory

# Global Variables
player_stats = {
    "health": 100,
    "strength": 10,
    "experience": 0,
    "weapon": "Basic Sword"
}
inventory = []
locations = {
    "start1": ["pond", "forest"],
    "start2": ["bunker", "neighborhood"],
    "pond": ["forest", "bunker"],
    "forest": ["airport1", "pond"],
    "bunker": ["airport2", "neighborhood"],
    "neighborhood": ["park", "start2"],
    "airport1": ["airport2", "forest"],
    "airport2": ["park", "bunker"],
    "park": ["neighborhood", "airport1"]
}
visited_locations = set()
enemies = {
    "forest": {"health": 50, "strength": 8},
    "bunker": {"health": 100, "strength": 12}
}
chests = {
    "pond": "Bomb",
    "neighborhood": "Health Potion",
    "bunker": "Special Weapon"  # Added for win condition
}
game_active = True  # Game state flag

# Functions
def display_stats():
    """Display player's current stats and inventory."""
    print("\nPlayer Stats:")
    for stat, value in player_stats.items():
        print(f"{stat.capitalize()}: {value}")
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}\n")

def access_inventory():
    """Allows the player to view and use items in the inventory."""
    if not inventory:
        print("Your inventory is empty.\n")
        return
    print("Your inventory contains:", ", ".join(inventory))
    choice = input("Do you want to use an item? (yes/no): ").strip().lower()
    if choice == "yes":
        item = input("Which item would you like to use? ").strip()
        if item in inventory:
            use_item(item)
        else:
            print("That item is not in your inventory.\n")
    else:
        print("You close your inventory.\n")

def use_item(item):
    """Use an item from the inventory."""
    if item == "Health Potion":
        player_stats["health"] = min(player_stats["health"] + 50, 100)
        print("You used a Health Potion. Health restored to:", player_stats["health"])
        inventory.remove(item)
    elif item == "Bomb":
        print("The Bomb is ready to be used in combat!")
    elif item == "Special Weapon":
        print("The Special Weapon is already equipped and powerful!")
    else:
        print("You can't use that item now.\n")

def move_to_location(current_location):
    """Allow player to move to a new location."""
    while True:
        print(f"You are at {current_location}. Possible paths: {locations[current_location]}")
        next_location = input("Where would you like to go? (or type 'inventory' to access your items): ").strip()
        if next_location.lower() == "inventory":
            access_inventory()
        elif next_location in locations[current_location]:
            return next_location
        else:
            print("Invalid location! Try again.\n")

def explore_location(location):
    """Explore the current location."""
    if location not in visited_locations:
        print(f"You explore the {location}...\n")
        # Handle enemy encounter
        if location in enemies:
            print(f"An enemy appears in the {location}!")
            combat(location)
        # Handle chest interaction
        if location in chests:
            item = chests[location]
            print(f"You find a chest with a {item}.")
            if input("Do you want to pick it up? (yes/no) ").lower() == "yes":
                pickup_item(item)
                del chests[location]
        visited_locations.add(location)
    else:
        print(f"You've already been to the {location}.\n")

def combat(location):
    """Handle combat mechanics."""
    enemy = enemies[location]
    print(f"Enemy Stats - Health: {enemy['health']}, Strength: {enemy['strength']}")
    while player_stats["health"] > 0 and enemy["health"] > 0:
        action = input("Do you want to attack, use inventory, or run? ").lower()
        if action == "attack":
            # Player attacks
            damage = player_stats["strength"]
            enemy["health"] -= damage
            print(f"You deal {damage} damage to the enemy.")
            # Enemy attacks
            if enemy["health"] > 0:
                enemy_damage = enemy["strength"]
                player_stats["health"] -= enemy_damage
                print(f"The enemy attacks and deals {enemy_damage} damage to you.")
        elif action == "use inventory":
            access_inventory()
        elif action == "run":
            print("You escaped the fight!")
            return
        else:
            print("Invalid action.")
    
    if player_stats["health"] <= 0:
        print("You have been defeated!")
        restart_game()
    elif enemy["health"] <= 0:
        print(f"You defeated the enemy in the {location}!")
        player_stats["experience"] += 50
        level_up()
        del enemies[location]

def pickup_item(item):
    """Add item to inventory and handle weapon upgrades."""
    inventory.append(item)
    print(f"You picked up a {item}.")
    if "weapon" in item.lower():
        print("Your weapon has been upgraded!")
        player_stats["weapon"] = item

def level_up():
    """Increase player stats when leveling up."""
    if player_stats["experience"] >= 100:
        player_stats["strength"] += 10
        player_stats["health"] += 20
        player_stats["experience"] -= 100
        print("You leveled up! Strength and health have increased.")

def restart_game():
    """Reset game state to start over."""
    global player_stats, inventory, visited_locations, game_active
    print("Restarting game...")
    player_stats = {"health": 100, "strength": 10, "experience": 0, "weapon": "Basic Sword"}
    inventory = []
    visited_locations = set()
    game_active = True

def main_menu():
    """Display main menu options."""
    print("Welcome to the Mystery Arena!")
    print("1. Start Game\n2. Quit\n3. Rules")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        return True
    elif choice == "2":
        print("Thanks for playing!")
        return False
    elif choice == "3":
        print("Explore, fight enemies, and uncover the mystery of the arena!")
        return main_menu()
    else:
        print("Invalid choice!")
        return main_menu()

# Main Game Loop
def main():
    global game_active
    current_location = "start1"  # Starting point

    if not main_menu():
        return

    while game_active:
        display_stats()
        explore_location(current_location)
        # Win condition
        if not enemies and "Special Weapon" in inventory:
            print("Congratulations! You have defeated all enemies and obtained the Special Weapon.")
            print("You uncovered the mystery of the arena and won the game!")
            break
        current_location = move_to_location(current_location)

# Run the game
if __name__ == "__main__":
    main()
