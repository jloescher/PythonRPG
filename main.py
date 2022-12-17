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



