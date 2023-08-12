
from AIPlayer1 import AIPlayer

def navigate_location(location, path):
    print(f"\nCurrent Location: {{path[-1]}}")
    options = list(location.keys())
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input(f"Choose a destination (1-{len(options)}), or 0 to go back: "))
    if choice == 0 and len(path) > 1:
        return path[:-1]  # Go back to the previous location
    elif 1 <= choice <= len(options):
        sub_location = options[choice - 1]
        path.append(sub_location)
        return path
    else:
        print("Invalid choice. Try again.")
        return path

def main():
    # Initialize the AIPlayer
    ai_player = AIPlayer(name="AI Explorer", setting="Virtual World", persona="Adventurer", goal="Exploration")

    # Fetch the directory structure
    directory_structure = ai_player.directory_structure
    print("Starting the adventure...")

    # Initialize the current location and path
    current_location = directory_structure['Virtual Forest - World Map']
    path = ['Virtual Forest - World Map']

    # Game Loop
    while True:
        # Navigate the current location
        path = navigate_location(current_location, path)

        # Update the current location based on the path
        current_location = directory_structure
        for loc in path:
            current_location = current_location[loc]

        # Check for quit condition (reached the root level)
        if len(path) == 1:
            print("Quitting the adventure.")
            break

if __name__ == "__main__":
    main()
