import random
username = input("What is your username? ")
races = [
        {"name": "Human", "hp": 100, "attack": 50},
        {"name": "Giant", "hp": 75, "attack": 125}
]
enemies = [
    {"Name": "Orc", "hp": 100, "attack": 10},
    {"Name": "Goblin", "hp": 120, "attack": 15},
    {"Name": "Skeleton", "hp": 75, "attack": 35}
]
inventory = []

race = random.choice(races)
gold = 100
enemy_fought = random.choice(enemies)
print(f"Welcome To The game {username}")
print(f"Your race is: {race["name"]}")

print("1. Explore")
print("2. Inventory")
print("3. Quit")

choice = input("Choose an option: ")
if choice == "1":
    print(f"You were exploring the area and suddenly a wild {enemy_fought["Name"]} appeared!")
    print("1. Stand your ground")
    print("2. Run Away and escape")
    enemy_encounter = input("What do you decide to do?")

    if enemy_encounter == "1":
        print(f"You decided to fight the wild {enemy_fought["Name"]}")

        player_hp = race["hp"]
        enemy_hp = enemy_fought["hp"]
        while player_hp > 0 and enemy_hp > 0:
            print(f"\nYour Hp: {player_hp}")
            print(f"{enemy_fought["Name"]} HP: {enemy_hp}")
            input("Press Enter to fight")
            enemy_hp -= race["attack"]
            print(f"You dealt {race['attack']} damage")
            if enemy_hp <= 0:
                print("You won,game over")
                break

            player_hp -= enemy_fought["attack"]
            print(f"The {enemy_fought['Name']} dealt {enemy_fought['attack']} back")
    else:
        print("You ran away successfully")
        
if choice == "2":
    print(f"Your inventory contains: {inventory}")
    input("Would you like to proceed to the shop (yes/no)?")
    if input().lower() == "yes":
        print("welcome to the shop!")
        store_choice = input("what would you like to buy?")
        print("1. Sword - 50 gold")
        print("2. Shield - 75 gold")
        print("3. Health Potion - 25 gold")
        print("4. Exit Shop")
if store_choice == "1":
    if gold >= 50:
        inventory.append("Sword")
        gold -= 50
        print("You bought a Sword!")
    else:
        print("Not enough gold!")

if store_choice == "2":
    if gold >= 75:
        inventory.append("Shield")
        gold -= 75
        print("You bought a Shield!")
    else:
        print("Not enough gold!")

if store_choice == "3":
    if gold >= 25:
        inventory.append("Health Potion")
        gold -= 25
        print("You bought a Health Potion!")
    else:
        print("Not enough gold!")

if store_choice == "4":
    print("Exiting the shop.")
if choice == "3":
    print("Thank you for playing KPG! Goodbye!")