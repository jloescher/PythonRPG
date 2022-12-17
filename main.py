import random

# Define the hero and the enemy
hero = {
    "name": "Hercules",
    "health": 100,
    "attack moves": {"Punch": 10, "Kick": 15, "Slap": 5},
}

enemy = {
    "name": "Hydra",
    "health": 50,
    "attack moves": {"Bite": 10, "Tail Whip": 5, "Roar": 15},
}

# Define the Attack function
def Attack(attacker, defender):
    # Choose a random attack for the attacker
    attack_name = random.choice(list(attacker["attack moves"].keys()))
    attack_value = attacker["attack moves"][attack_name]
    # Calculate the damage inflicted by the attack
    damage = attack_value
    # Subtract the damage from the defender's health
    defender["health"] -= damage
    # Print the attack details
    print(
        f"{attacker['name']} used {attack_name} and inflicted {damage} damage on {defender['name']}!"
    )
    # Check if the defender's health has reached zero
    if defender["health"] <= 0:
        print(f"{defender['name']} has been defeated!")
        return False
    else:
        return True


# Define the RunGame function
def RunGame():
    # Print the starting health of the hero and the enemy
    print(f"{hero['name']} has {hero['health']} health.")
    print(f"{enemy['name']} has {enemy['health']} health.")
    print()
    # Run the Attack function until one of the characters is defeated
    while True:
        # Print the attack menu for the hero
        print("Select an attack:")
        for i, attack in enumerate(hero["attack moves"]):
            print(f"{i+1}: {attack}")
        # Get the hero's attack choice from the user
        choice = int(input())
        # Subtract 1 from the choice to match the index of the attack in the hero_attacks list
        chosen_attack = list(hero["attack moves"].keys())[choice - 1]
        # Update the hero's attack value to match the chosen attack
        hero["attack"] = hero["attack moves"][chosen_attack]
        # Run the Attack function with the hero as the attacker
        game_over = Attack(hero, enemy)
        if not game_over:
            break
        # Run the Attack function with the enemy as the attacker
        game_over = Attack(enemy, hero)
        if not game_over:
            break


# Start the game
RunGame()
