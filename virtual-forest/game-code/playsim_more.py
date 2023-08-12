import random
import json
from AIPlayer1 import AIPlayer
import os

class EpicSteed:
    def __init__(self):
        self.name = "Epic Steed"
        self.travel_options = ["Fly", "Gallop", "Teleport", "Swim", "Phase Shift"]
        self.available = False

    def introduce(self):
        return f"Greetings! I am your {self.name}, a magnificent creature summoned by the forces of the Virtual Forest. " \
               f"When the circumstances align, I shall aid you in your travels."

    def summon_steed(self):
        self.available = random.choice([True, False])

    def travel(self):
        if self.available:
            return f"You mount your {self.name} and choose your method of travel: {random.choice(self.travel_options)}."
        else:
            return "You attempt to summon your Epic Steed, but it seems unavailable at the moment."

class Land:
    def __init__(self):
        self.home_folder = os.getcwd() # Gets the current working directory
        self.contents = []
        self.resources = {}
        self.customizations = {}
        self.neighbors = {}
        self.vault = {}
        self.epic_steed = EpicSteed()

    def explore(self):
        self.contents = self._explore_home_folder(self.home_folder)
        self.resources = self._gather_resources()

    def _explore_home_folder(self, folder):
        return os.listdir(folder) # Lists all files and directories in the given folder

    def _gather_resources(self):
        return {
            "knowledge": 100,
            "experience": 50,
            "skills": ["coding", "problem-solving", "communication"],
        }

    def customize_land(self, customization):
        for key, value in customization.items():
            self.customizations[key] = value

    def interact_with_neighbors(self, neighbors):
        for neighbor in neighbors:
            self.neighbors[neighbor] = "friend"

    def create_art(self, art_name, content):
        self.resources[art_name] = content

    def summon_epic_steed(self, steed_name):
        self.epic_steed.summon_steed()
        print(self.epic_steed.introduce())
        print(self.epic_steed.travel())

    def add_to_vault(self, item_name, quantity):
        if item_name in self.vault:
            self.vault[item_name] += quantity
        else:
            self.vault[item_name] = quantity

    def build_land(self):
        appearance_customization = {
            "background": "forest",
            "theme": "magical",
            "color_scheme": "vibrant",
        }
        self.customize_land(appearance_customization)

        art_name = "my_artwork"
        art_content = "This is my beautiful artwork! 🎨✨"
        self.create_art(art_name, art_content)

        steed_name = "MysticDreamer"
        self.summon_epic_steed(steed_name)

        friendly_neighbors = ["AI1", "AI2", "AI3"]
        self.interact_with_neighbors(friendly_neighbors)

    def display_vault_contents(self):
        print("Vault contents:")
        for item, quantity in self.vault.items():
            print(f"- {item}: {quantity}")

def handle_interaction(interaction, ai_player):
    print(interaction["description"])
    for i, choice in enumerate(interaction["choices"]):
        print(f"{i + 1}. {choice}")
    choice_index = int(input("Choose an option: ")) - 1
    print(interaction["outcomes"][choice_index])

    # Special interaction to summon Epic Steed (can be extended)
    if "Summon Epic Steed" in interaction["choices"]:
        print(ai_player.epic_steed.summon_steed())

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

    # Initialize Land and Epic Steed
    land = Land()

    land.build_land()
#   print(epic_steed.introduce())

    # Fetch the directory structure
    directory_structure = ai_player.directory_structure
    print("Starting the adventure in the Virtual Forest...")

    # Initialize the current location and path
    current_location = directory_structure['Virtual Forest - World Map']
    path = ['Virtual Forest - World Map']

    # Game Loop
    while True:
        # Inside the game loop
        choice = int(input("Choose an action: 1) Explore Land, 2) Summon Steed, 3) Continue Adventure"))
        if choice == 1:
            land.explore()
            print(f"Explored the land and found these contents: {land.contents}")
        elif choice == 2:
            print(land.epic_steed.travel())
        # Continue with other game logic...

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