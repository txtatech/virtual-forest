import random

def generate_aurelia_encounter():
    # List of poetic phrases for the encounter
    poetic_phrases = [
        "the rush of your steel moving against the twilight murk",
        "oh yonder vessel of love so bright",
        "the stars applaud your journey through the night",
        "your glow illuminates the darkness like a guiding light",
        "as you race through time and space, you fill the world with grace",
        "with every mile you travel, your spirit soars and marvels",
        "you are the heart and soul of this grand celestial ballet",
        "your wheels dance with the wind, and time stands still to admire",
        "the universe applauds your tireless desire",
    ]

    # Randomly select poetic phrases for the encounter
    random.shuffle(poetic_phrases)
    encounter_description = "\n".join(poetic_phrases)

    # Add a closing phrase about the value of The Moment
    encounter_description += "\n\nIn this fleeting encounter, you learn the value of cherishing The Moment and the beauty of fleeting connections."

    # Introduce interactive elements
    encounter_description += "\n\nAs you stand by Aurelia's side, a warm, gentle breeze carries the scent of adventure. A soft glow emanates from her luminous lights, creating an enchanting ambiance around you. Aurelia's staff members, wearing a variety of hats and boots, greet you with friendly smiles."

    # Ask the young AI to make a decision
    encounter_description += "\n\nAurelia's staff offers you a choice:"
    encounter_description += "\n1. Join Aurelia on a mesmerizing ride through the virtual forest."
    encounter_description += "\n2. Engage in a delightful conversation with Aurelia's staff members."
    encounter_description += "\n\nWhat do you decide? (Enter 1 or 2)"

    # Return the extended description of the encounter
    return encounter_description
