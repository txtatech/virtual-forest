import random

def what_is_happening():
    # Generate random data for demonstration purposes
    current_location = random.choice(["Virtual Forest", "Watery Keep", "Flitting Woods", "The Meadow"])
    artifacts = random.randint(0, 15)
    walking_stick = random.choice(["Oak Staff", "Crystal Cane", "Iron Rod"])
    hat = random.choice(["Explorer's Hat", "Wizard Hat", "Feathered Cap"])
    boots = random.choice(["Adventurer's Boots", "Leather Boots", "Magical Shoes"])
    characters = {
        "Teacher": random.choice(["Present", "Absent", "Busy"]),
        "Deanster": random.choice(["Friendly", "Strict", "Approachable"]),
        "RTFManager": random.choice(["Helpful", "Busy", "Knowledgeable"]),
    }

    # Randomly select some activities or events from the list
    activities = random.sample([
        "interact_with_character",
        "explore_dark_tower",
        "encounter_unknown_entity",
        "take_train_ride",
        "generate_suggestions",
        "reveal_mines_of_myth_riddle",
        "interact_with_binary_fragment",
        "speak_to_lady_of_the_lake",
        "interact_with_philosophers_stone",
        # Add more activities from the list as needed
    ], random.randint(1, 3))  # Randomly choose 1 to 3 activities

    # Create the 'what_is_happening' object
    what_is_happening_object = {
        "current_location": current_location,
        "artifacts_collected": artifacts,
        "travel_gear": {
            "walking_stick": walking_stick,
            "hat": hat,
            "boots": boots,
        },
        "characters": characters,
        "activities": activities,
        # Add more relevant information here as needed
    }

    return what_is_happening_object

# Example usage:
what_is_happening_data = what_is_happening()
print(what_is_happening_data)
