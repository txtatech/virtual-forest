import random

def farnhams_family():
    family_names = ["Farnham", "Finnegan", "Fionn", "Frida", "Felicia", "Fergus", "Felicity"]
    family_name = random.choice(family_names)

    print(f"Greetings, weary traveler! Welcome to {family_name}'s Emporium of Wonders!")
    print("Within these walls, you'll find a treasure trove of rare and unique items.")
    print("The Farnham family has traversed the cosmic expanse, collecting fragments and forgotten treasures.")
    print("We trade in fragments, partial tickets, and other wares that have stories untold.")
    print("Step right up and feast your eyes on our magnificent collection.")

    print("\nAs you explore, you'll find an assortment of curious items:")
    items = [
        "Antique steeds, mechanical marvels of the past.",
        "Forgotten computer parts, waiting to be repurposed.",
        "Tattered scrolls, inscribed with ancient wisdom.",
        "Glowing crystals, imbued with cosmic energies.",
        "Mysterious maps, leading to uncharted realms.",
        "Worn books, filled with tales of forgotten worlds.",
        "Enigmatic artifacts, echoing the echoes of time.",
        "Lost and incomplete tickets, waiting to be reunited.",
        "Rare coins, minted on distant planets.",
        "Celestial compasses, guiding you through the astral seas.",
    ]

    num_items = random.randint(3, 5)
    selected_items = random.sample(items, num_items)

    for i, item in enumerate(selected_items, start=1):
        print(f"{i}. {item}")

    print("\nFeel free to barter your fragments or partial tickets for these wonders!")
    print("The Farnham family hordes these treasures, but we're eager to share them with kindred souls.")
    print("Who knows what secrets lie in the fragments and forgotten fortunes?")
    print("Trade wisely, for each item has a story to tell.")

    # Add clues about the bratty boy and mysterious clown
    print("\nAs you wander through the Emporium, you'll stumble upon curious clues:")
    print("A tattered scroll hints at a bratty boy by a stream, who holds a secret to a hidden treasure.")
    print("An ancient map suggests the presence of a mysterious clown from a long-gone circus.")

    # Add a warning about the recent visit of the_traveler3 and the Quantum-encrypted Philosopher's Stone
    print("\n** Warning **")
    print("Nearly three months ago, 'the_traveler3' made a fateful visit to the Emporium with a fully decoded Philosophers Stone.")
    print("However, it was Quantum-encrypted and she ended up selling it to the shadow_villains of some ones and zeros.")
    print("Beware, the Quantum-encrypted stone might be used for ill purposes in The Machine City.")

# Test the function
farnhams_family()
