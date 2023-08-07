import random

def band_of_heroes(young_ai_name):
    # List of disguised characters in the band of heroes
    heroes = [
        "Valiant Knight",
        "Fearless Archer",
        "Mystic Sorceress",
        "Swift Ranger",
        "Resolute Guardian",
        "Courageous Paladin"
    ]

    # Randomly shuffle the list of heroes
    random.shuffle(heroes)

    # Define the number of heroes with all powers (minimum 1 and maximum the number of heroes)
    num_heroes_with_all_powers = random.randint(1, len(heroes))

    # Create a set to store the indices of heroes with all powers
    heroes_with_all_powers_indices = set()

    # Randomly select the indices of heroes with all powers
    while len(heroes_with_all_powers_indices) < num_heroes_with_all_powers:
        heroes_with_all_powers_indices.add(random.randint(0, len(heroes) - 1))

    # Define a dictionary of potential heroic actions the band can take
    actions = {
        "Assist": f"The {hero} and the Band of Heroes arrive to provide much-needed assistance!",
        "Inspire": f"The {hero} and the Band of Heroes inspire {young_ai_name}, boosting their confidence and resolve.",
        "Shield": f"The {hero} and the Band of Heroes form a protective shield, keeping {young_ai_name} safe from harm.",
        "Unite": f"The {hero} and the Band of Heroes unite their strengths, overcoming a formidable challenge.",
        "Renew": f"The {hero} and the Band of Heroes bestow renewed energy and vigor upon {young_ai_name}."
    }

    # Define a dictionary to store the powers of each hero
    hero_powers = {}

    # Assign powers to each hero
    for i, hero in enumerate(heroes):
        # Randomly select an action from the dictionary
        action = random.choice(list(actions.keys()))

        # Ensure that a hero with all powers has the power of "All"
        if i in heroes_with_all_powers_indices:
            hero_powers[hero] = "All"
        else:
            hero_powers[hero] = action

    # Perform the selected action based on each hero's powers
    hero = random.choice(heroes)
    action = hero_powers[hero]
    result = actions[action]

    return result
