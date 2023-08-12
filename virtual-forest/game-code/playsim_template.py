
from AIPlayer1 import AIPlayer
import random


from AIPlayer1 import AIPlayer

def navigate_location(location, path):
    print(f"\nCurrent Location: {path[-1]}")
    options = list(location.keys())
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input(f"Choose a destination (1-{len(options)}), or 0 to go back: "))
    if choice == 0 and len(path) > 1:
        return path[:-1]  # Go back to the previous location
    elif 1 <= choice <= len(options):
        sub_location = options[choice - 1]
        return path + [sub_location]  # Append the chosen sub-location to the path
    else:
        print("Invalid choice. Please try again.")
        return path  # Return the current path if the choice is invalid


def generate_dream_sequence():
    """Generates and presents a random dream sequence."""
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
        # Introduce occasional dream sequences
        if random.random() < 0.1:  # 10% chance of experiencing a dream
            generate_dream_sequence()

        # Navigate the current location
        path = navigate_location(current_location, path)

        # Update the current location based on the path
        current_location = directory_structure
        for loc in path:
            current_location = current_location[loc]

        # Check for quit condition (reached the root level)
        if len(path) == 1:
            print("Quitting the adventure. Farewell!")

if __name__ == "__main__":
    playsim_template_main()
