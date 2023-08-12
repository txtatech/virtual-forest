import json
import random
from AIPlayer1 import AIPlayer

def handle_interaction(interaction):
    print(interaction["description"])
    for i, choice in enumerate(interaction["choices"]):
        print(f"{i + 1}. {choice}")
    choice_index = int(input("Choose an option: ")) - 1
    print(interaction["outcomes"][choice_index])

def navigate_location(location, path):
    print(f"\nDebug: Path before navigation: {path}")
    if not path:
        print("Debug: Path is empty. Returning default path.")
        return ['Virtual Forest - World Map']
    print(f"Current Location: {path[-1]}")
    options = list(location.keys())
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input(f"Choose a destination (1-{len(options)}), or 0 to go back: "))
    print(f"Debug: Choice made: {choice}")
    if choice == 0 and len(path) > 1:
        return path[:-1]
    elif 1 <= choice <= len(options):
        sub_location = options[choice - 1]
        return path + [sub_location]
    else:
        print("Invalid choice. Please try again.")
        return path

def generate_dream_sequence():
    dream_scenarios = [
        "The Enchanted Oasis",
        "The Starlit Symphony",
        "The Whispering Grove",
        "The Dancing Shadows",
    ]
    dream_choice = random.choice(dream_scenarios)
    print(f"You experience a dream: {dream_choice}")
    print("The echoes of the dream linger as you wake up and return to the Virtual Forest.")

def playsim_template_main():
    # Initialize the AIPlayer
    ai_player = AIPlayer(name="AI Explorer", setting="Virtual World", persona="Adventurer", goal="Exploration")

    # Fetch the directory structure
    directory_structure = ai_player.directory_structure
    print("Starting the adventure in the Virtual Forest...")

    # Initialize the current location and path
    current_location = directory_structure['Virtual Forest - World Map']
    path = ['Virtual Forest - World Map']

    # Game Loop
    while True:
        # Randomly introduce dream sequences
        if random.random() < 0.1:
            generate_dream_sequence()

        # Navigate the current location
        path = navigate_location(current_location, path)

        # Update the current location based on the path
        current_location_name = path[-1]
        current_location = directory_structure
        for loc in path:
            current_location = current_location[loc]

        # Generate and handle a random interaction
        interaction = ai_player.generate_interaction(current_location_name) # Call through AIPlayer instance
        ai_player.handle_interaction(interaction)

        # Check for quit condition (reached the root level)
        if len(path) == 1:
            print("Quitting the adventure. Farewell!")
            break

        # Update game state based on interaction outcomes (to be implemented)
        # Save game state to AI_state.json (to be implemented)

# Run the main game loop
playsim_template_main()
