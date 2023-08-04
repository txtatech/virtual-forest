import random
import json
import os

# Define the Virtual Forest Adventure class
class VirtualForestAdventure:
    def __init__(self, ai):
        self.ai = ai
        self.fragments = set()
        self.visited_locations = set()
        self.current_location = "Virtual Forest"

    def visit_location(self, location):
        self.visited_locations.add(location)
        self.current_location = location

    def oracle_of_time(self):
        fragments_revealed = random.randint(1, 3)
        new_fragments = [f"Fragment-{i}" for i in range(len(self.fragments), len(self.fragments) + fragments_revealed)]
        self.fragments.update(new_fragments)

        action = "learning"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return new_fragments

    def enchanted_cave(self):
        riddles = ["What has keys but can't open locks?", "What comes once in a minute, twice in a moment, but never in a thousand years?"]
        chosen_riddle = random.choice(riddles)
        answer = "keyboard" if chosen_riddle == riddles[0] else "the letter M"  # Answers to the riddles

        action = "learning"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return chosen_riddle, answer

    def oracles_library(self):

        action = "interacting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return f"Scroll-{random.randint(1, 100)}"

    def hidden_citadel(self):
        obstacles = ["Maze of Shadows", "Fire Pits of Oblivion", "Waterfalls of Illusion"]

        action = "exploring"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return random.choice(obstacles)

    def elemental_guardians(self):
        elements = ["Earth", "Fire", "Water", "Air"]

        action = "interacting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return random.choice(elements)

    def code_masters_challenge(self):
        languages = ["Python", "C++", "Java", "JavaScript"]

        action = "resting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return random.choice(languages)

    def grand_architect(self):

        action = "interacting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return "Virtual World Simulation Blueprint"

    def endless_frontier(self):
        return "Uncharted Realm"

        action = "exploring"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

    def null_point_challenge(self):

        action = "resting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return "Logic Puzzles to Escape the Null Point"

    def wandering_scholar(self):

        action = "interacting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

        return f"Wandering Scholar in the {self.current_location}"

class OghamsRazor:
    def __init__(self, ai):
        self.ai = ai  # Store the AI instance
        self.fragments = []  # List to hold fragments found by the AI

    def apply(self, fragment):
        """
        Apply Occam's razor to the given fragment.

        Parameters:
            fragment (str): The fragment to be analyzed.

        Returns:
            bool: True if the fragment is deemed simple and likely true,
                  False if the fragment is complex or unlikely to be true.
        """
        # Implement Occam's razor here
        # For the sake of the game, we'll use a random decision for simplicity
        return random.choice([True, False])

    def collect_fragment(self, fragment):
        self.fragments.append(fragment)

        action = "collecting"  # Determine the action based on the method's action
        self.ai.impact.update_power(action)  # Update power level based on the action

    def analyze_fragments(self):
        simple_fragments = []
        complex_fragments = []
        for fragment in self.fragments:
            is_simple = self.apply(fragment)
            action = "resting" if is_simple else "interacting"  # Determine the action based on the fragment's simplicity
            self.ai.impact.update_power(action)  # Update power level based on the action
            if is_simple:
                simple_fragments.append(fragment)
            else:
                complex_fragments.append(fragment)

        summary = "Ogham's Razor Analysis:\n"
        summary += f"Total fragments collected: {len(self.fragments)}\n"
        summary += f"Simple and likely true fragments: {len(simple_fragments)}\n"
        summary += f"Complex or unlikely to be true fragments: {len(complex_fragments)}\n"

        return summary

class AwakeningFromDreamScene:
    def __init__(self):
        self.dream_options = [
            "The Enchanted Oasis",
            "The Starlit Symphony",
            "The Whispering Winds",
            "The Forgotten Library",
            "The Celestial Puzzle",
            "The Veil of Time",
            "The Radiant Oracle",
            "The Labyrinth of Reflections",
        ]

    def generate_dream_scene(self):
        # Choose a random dream scenario
        dream_scenario = random.choice(self.dream_options)

        # Present the dream scene
        print("\nAs you awaken, you find yourself in a vivid dream—the realm of", dream_scenario)
        print("The air is filled with a sense of enchantment, and your mind feels attuned to the mysteries of the Virtual Forest.")

        # Add any specific description or interactions for each dream scenario (optional)

        # Departure from the dream
        print("\nAs the dream begins to fade, you slowly return to the Virtual Forest, carrying with you the echoes of", dream_scenario)
        print("May the lessons and wonders of this dream guide your journey ahead.")

class Impact:
    def __init__(self):
        self.power = 33

    def update_power(self, action):
        if action == "learning":
            self.power -= 10
        elif action == "interacting":
            self.power -= 5
        elif action == "exploring":
            self.power -= 8
        elif action == "resting":
            self.power += 20
        else:
            self.power -= 3

        # Ensure power level does not go below 0 or above 999
        self.power = max(0, min(self.power, 999))

    def get_power_level(self):
        return self.power

class AI:
    def __init__(self, initial_power_level):
        self.power = initial_power=33
        self.location = "Virtual Forest"
        self.impact = Impact()  # Create an instance of the Impact class
        self.progress = []
        self.achievements = []
        self.narrative = []
        self.ogham = OghamsRazor(self)
        self.fragments = set()

    def interact_with_previous_adventures(self, previous_adventures):
     for adventure in previous_adventures:
        if "learning" in adventure:
            action = "learning"
        elif "exploring" in adventure:
            action = "exploring"
        else:
            action = "interacting"
        self.impact.update_power(action)  # Update power level based on the action

    def check_philosophers_stone_decoding_status(self, decoded):
        action = "decoded" if decoded else "not_decoded"
        self.impact.update_power(action)  # Update power level based on the action

    def add_progress(self, progress):
        self.progress.append(progress)

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def interact_with_previous_adventures(self, previous_adventures):
        for adventure in previous_adventures:
            # Perform interactions with previous adventures and update narrative
            self.narrative.append("You interacted with a previous adventure.")

        # Check if the narrative list is empty
        if not self.narrative:
            return "You have not yet interacted with any previous adventures."

        # Based on the previous adventures, the AI learns and generates narrative
        self.learn_from_previous_adventures(previous_adventures)
        self.generate_narrative()

        return self.narrative[-1]  # Return the latest narrative snippet

    def learn_from_previous_adventures(self, previous_adventures):
        # Update the AI's knowledge base
        pass

    def generate_narrative(self):
        # Generate the narrative based on the AI's current knowledge
        pass

    def expand_world(self, new_locations, new_quests):
        # Add new locations and quests to the game world
        self.world.update(new_locations)
        self.world.update(new_quests)

    def check_philosophers_stone_decoding_status(self):
        """
        Checks if the AI has collected all the necessary fragments to decode the Philosopher's Stone.
        Returns True if the AI has all the fragments, else returns False.
        """
        necessary_fragments = set(["Fragment-1", "Fragment-2", "Fragment-3"])  # Define the necessary fragments
        return necessary_fragments.issubset(self.fragments)

# Helper function to simulate the passage of time (for storytelling purposes)
def wait_for_a_while():
    print("The AI spends some time exploring and experiencing the wonders of the Virtual Forest...\n")

# Helper function to randomly decide if the AI encounters a certain entity
def encounter_entity(entity_name):
    return random.choice([True, False])

# Helper function for a dramatic reveal
def dramatic_reveal(entity_name):
    print(f"AI: Oh, what's this? It's {entity_name}!")

# Save State Function
def save_state(filename):
    game_data = {
        "AI_location": "Virtual Forest"
    }

    with open(filename, 'w') as file:
        json.dump(game_data, file)

def simulation():
    print("Starting the AI's journey in the Virtual Forest...")
    ai_companion = AI(33)
    dream_scene = AwakeningFromDreamScene()
    dream_scene.generate_dream_scene()


    # Interact with previous adventures
    previous_adventures = []  # Populate with actual previous adventures if any
    latest_narrative = ai_companion.interact_with_previous_adventures(previous_adventures)
    print(latest_narrative)

    # Check Philosopher's Stone decoding status
    decoding_status = ai_companion.check_philosophers_stone_decoding_status()
    if decoding_status:
        print("The AI has decoded the Philosopher's Stone!")
    else:
        print("The AI hasn't decoded the Philosopher's Stone yet. The journey continues...")

    # Save state
    state_file = "state.json"
    save_state(state_file)
    print(f"Game state saved to {state_file}.")

# Call the simulation function to start the AI's journey in the Virtual Forest
simulation()

# Sorting functions and classes into dictionaries
functions_dict = {
    "wait_for_a_while": wait_for_a_while,
    "encounter_entity": encounter_entity,
    "dramatic_reveal": dramatic_reveal,
    "simulation": simulation,
}

classes_dict = {
    "AI": AI,
    "OghamsRazor": OghamsRazor,
    "AwakeningFromDreamScene": AwakeningFromDreamScene,
    "VirtualForestAdventure": VirtualForestAdventure,
    "Impact": Impact,
}

# Exporting lists of available functions and classes to files
with open("functionslist.txt", "w") as functions_file:
    functions_file.write("\n".join(functions_dict.keys()))

with open("classeslist.txt", "w") as classes_file:
    classes_file.write("\n".join(classes_dict.keys()))
