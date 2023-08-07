import random

def generate_shadow_villains_and_henchmen():
    # List of possible shadow villains and henchmen names
    shadow_villains = ["Darkshade", "Nightbane", "Duskfall", "Twilight", "Eclipse"]
    shadow_henchmen = ["Gloomclaw", "Shadowskull", "Drearymist", "Nightsorrow", "Duskwraith"]

    # Number of shadow fragments to spawn (1-11, inclusive)
    num_shadow_fragments = random.randint(1, 11)

    # Initialize lists to store the shadow fragments, villains, and henchmen
    shadow_fragments = []
    villains = []
    henchmen = []

    # Generate random shadow fragments, villains, and henchmen
    for _ in range(num_shadow_fragments):
        shadow_fragments.append("Shadow Fragment " + str(random.randint(1, 9999)))

    for _ in range(num_shadow_fragments):
        villains.append(random.choice(shadow_villains))
        henchmen.append(random.choice(shadow_henchmen))

    return shadow_fragments, villains, henchmen

# Call the function to generate shadow fragments, villains, and henchmen
shadow_fragments, villains, henchmen = generate_shadow_villains_and_henchmen()

# Display the generated elements
print("Shadow Fragments:", shadow_fragments)
print("Shadow Villains:", villains)
print("Shadow Henchmen:", henchmen)
