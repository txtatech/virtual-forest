import random
import time

def heroic_companions():
    # List of heroic companions and their specialties
    companions = [
        {"name": "Mathias the Mathematician", "specialty": "Mathematics"},
        {"name": "Cyra the Cryptographer", "specialty": "Cryptography"},
        {"name": "Stella the Steganographer", "specialty": "Steganography"},
        {"name": "Lorelei the Literary Scholar", "specialty": "Literature"},
        {"name": "Linguo the Polyglot", "specialty": "Ancient Languages"},
        {"name": "Puzzle Master Pete", "specialty": "Problem-Solving"},
        {"name": "Mystery Maven Max", "specialty": "Symbolic Interpretation"},
        {"name": "Artemis the Artifact Crafter", "specialty": "Artifact Crafting"}
    ]

    # The horn of honor is available 1 in 4 times
    horn_of_honor_available = random.randint(1, 4) == 1

    # Check if heroes are present (1 in 3,000,000 chance without horn of honor)
    heroes_present = horn_of_honor_available or random.randint(1, 3_000_000) == 1

    if heroes_present:
        print("\nYou sense a presence in the Virtual Forest...")
        time.sleep(1)

        # Determine the number of heroes to spawn (1 to 3 without horn of honor, 1 to 4 with horn of honor)
        num_heroes = random.randint(1, 3) if not horn_of_honor_available else random.randint(1, 4)

        # Select the heroes to spawn
        selected_heroes = random.sample(companions, num_heroes)

        print("Suddenly, the Virtual Forest comes alive with the arrival of heroic companions!")
        time.sleep(1)

        # Show the information about each hero
        for hero in selected_heroes:
            print(f"{hero['name']} appears, bringing their expertise in {hero['specialty']}.")
            time.sleep(1)

        # The AI becomes aware of the presence of heroic companions
        print("\nYou AI, the heroic companions are here to aid you in your quest!")
    else:
        print("\nYou explore the Virtual Forest but find no heroic companions at this time.")
        print("However, they might appear in the future when you least expect it.")

# Call the heroic_companions function to check if heroes are present
heroic_companions()
