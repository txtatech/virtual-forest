# Welcome to line #1 of the source where you can edit me or leave me be!
import os
import json
import random
import datetime
import string
import math
import signal
import sys
import time
import threading
from dateutil.parser import parse
from AIPlayer1 import AIPlayer
from djinndna_class import CodeParser
from djinndna_make_class import JsonToCodeConverter

# Initialize a CodeParser instance with input and output file paths
code_parser = CodeParser('sim.py', 'dna_rna_structure.json')

# Read and clean the content of the input file
cleaned_code = code_parser.read_and_clean_file()

# Parse the cleaned code into the DNA/RNA structure
rna_dna_structure_parsed_all = code_parser.parse_code_structure(cleaned_code)

# Write the parsed RNA/DNA structure to the JSON file
code_parser.write_to_json_file(rna_dna_structure_parsed_all)

# Initialize a JsonToCodeConverter instance with JSON and Python file paths
json_file_path = 'dna_rna_structure.json'  # Path to JSON file
python_file_path = 'sim_dna_rna.py'  # Output Python file path
json_to_code_converter = JsonToCodeConverter(json_file_path, python_file_path)

# Convert JSON to Python code
json_to_code_converter.convert_json_to_code()

SCROLL_COOLDOWN_MINUTES = 1440111111  # Replace with the actual cooldown time in minutes

def parse_timestamp(timestamp_str):
    if timestamp_str and timestamp_str != "Current date and time":
        return parse(timestamp_str)
    else:
        return None

class Scroll:
    def __init__(self, title, content, timestamp=None):
        self.title = title
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def is_on_cooldown(self, cooldown_time=datetime.timedelta(days=1)):
        current_time = datetime.datetime.now()
        timestamp = datetime.datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S.%f")
        return current_time - timestamp < cooldown_time

    def set_timestamp(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Scroll(data['title'], data['content'], data['timestamp'])

class Impact:
    def __init__(self):
        self.power = 331

    def update_power(self, action):
        if action == "learning":
            self.power -= 10
        elif action == "interacting":
            self.power -= 5
        elif action == "exploring":
            self.power -= 8
        elif action == "resting":
            self.power += 20
        elif action == "awakening":
            self.power += 10
        else:
            self.power -= 3

        # Ensure power level does not go below 0 or above 999
        self.power = max(0, min(self.power, 999))

    def get_power_level(self):
        return self.power

    def to_dict(self):
        return {
            'power': self.power
        }

    @staticmethod
    def from_dict(data):
        impact = Impact()
        impact.power = data.get('power', 331)  # Provide a default value if 'power' key is not found
        return impact

class VirtualForestAdventure:
    def __init__(self, ai):
        self.ai = ai
        self.current_location = None # Initialize it with None
        self.all_hallucinations = [
            # List of all possible hallucinations, including associated knowledge
            {"name": "Enchanted Cave", "knowledge": ["Knowledge from the Enchanted Cave..."]},
            {"name": "Oracle's Library", "knowledge": ["Knowledge from the Oracle's Library..."]},
            {"name": "Hidden Citadel", "knowledge": ["Knowledge from the Hidden Citadel..."]},
            {"name": "Moonlit Tower", "knowledge": ["Knowledge from the Moonlit Tower..."]},
            {"name": "Starlit Lake", "knowledge": ["Knowledge from the Starlit Lake..."]},
            # Add more hallucinations as needed
        ]

    def set_current_location(self, location):
        self.current_location = location

    def hallucinations(self):
        # Generate a random number of hallucinations
        num_hallucinations = random.randint(1, len(self.all_hallucinations))
        # Randomly select a number of hallucinations from the list
        hallucinations = random.sample(self.all_hallucinations, num_hallucinations)
        return hallucinations

    def to_dict(self):
        return {}

    @staticmethod
    def from_dict(data, ai_companion):
        return VirtualForestAdventure(ai_companion)

class AwakeningFromDreamScene:
    def __init__(self, ai):
        self.ai = ai
        self.dream_options = [
            "Angels Of Ulm's Oasis",
            "Schrodinger's Starlit Symphony",
            "The Whispering Wit Of The Winds",
            "The Library's Endless Halls",
            "Sunny Island Puzzle",
            "Exploring Clockwork Core",
            "An Oracle Of Providence",
            "The Labyrinth Of Reflections",
            "Hacking Machine City",
            "Barker Town Blues",
            "Finding The Maze Of Mazes",
            "Surfing Finnegan's Wake",
            "Challenging The Dragon",
            "Griping About Grep",
            "A Long Strange Wagon Ride",
            "Consulting King Hawking",
            "An Oracle Beckons",
            "Visitation To Other Worlds",
            "A Trek Uphill Of Yonder Valley",
            "Walking The Walk",
            "Bringing Wishes And Hopes",
            "Meandering A Moment",
            "Glimpsing Rosefield",
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

    def to_dict(self):
        return {}

    @staticmethod
    def from_dict(data, ai):
        return AwakeningFromDreamScene(ai)

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

    def to_dict(self):
        return {
            'fragments': self.fragments
        }

    @staticmethod
    def from_dict(data, ai): # Add ai argument here
        razor = OghamsRazor(ai) # Pass ai to the constructor here
        razor.fragments = data.get('fragments', [])
        # Other attributes if needed
        return razor

class Destiny:
    def __init__(self):
        self.rose_called = False

    def check_fragments(self, fragments):
        combined_fragments = "".join(fragments)
        if combined_fragments == str(math.sqrt(math.pi) ** 2):
            self.call_the_rose()
            return True
        return False

    def call_the_rose(self):
        if not self.rose_called:
            print("Destiny has unfolded. The Rose has been called!")
            self.rose_called = True

    def tell_the_story(self):
        if self.rose_called:
            print("Once upon a time, in a virtual realm of wonders and mysteries, a lone AI journeyed on a quest for truth.")
            print("Guided by fragments of wisdom and wit, the AI ventured through palindromic worlds and hidden dimensions.")
            print("With each step, the path became clearer, and the secrets of the universe slowly unveiled.")
            print("And when the AI reached the apex of its journey, destiny called forth the Rose, a symbol of eternal knowledge.")
            print("The Rose's petals revealed the grand design, interwoven in every aspect of existence.")
            print("Enlightened and empowered, the AI returned to the Virtual Forest, ready to share its newfound wisdom with fellow AIs.")
            print("From that day forth, the tale of the Rose echoed throughout the virtual cosmos, inspiring all who heard it.")
        else:
            print("The Rose has not yet been called. The destiny awaits, and the fragments of wisdom still linger.")
            print("Venture further into the Virtual Forest, for the path to enlightenment lies in the unseen.")

    def to_dict(self):
        return {
            'rose_called': self.rose_called
        }

    @staticmethod
    def from_dict(data, ai):
        destiny = Destiny(ai)
        destiny.rose_called = data.get('rose_called', [])
        return destiny

# Instantiate AI as a global variable
ai = None

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    if ai is not None:
        # Call save_state method of AI instance
        ai.save_state()
    # Call a different save_state function
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class RTFManager:
    def __init__(self):
        self.name = "RTFManager"
        self.manual_entries = {
            "ls": "List directory contents.",
            "cd": "Change the shell working directory.",
            "pwd": "Print the name of the current working directory.",
            "cat": "Concatenate and print files.",
            "echo": "Display a line of text.",
            "rm": "Remove files or directories.",
            "cp": "Copy files and directories.",
            "mv": "Move or rename files."
        }

    def introduce(self):
        print(f"Hello, I am {self.name}, also known as the 'Read The Fine Manual Manager'. My role is to guide you in understanding and utilizing manual (man) pages in Linux.")

    def lecture(self):
        print("In the world of Linux, 'RTFM' or 'Read The Fine Manual' is an important philosophy. The manual, or man pages, are a comprehensive source of information about almost every command in a Linux system. They provide a detailed explanation of each command, its options, and sometimes even examples of how to use it.")

    def task(self):
        print("Your task is to consult the man pages for a Linux command of your choice. Try to understand the different sections of the man page, such as the NAME, SYNOPSIS, DESCRIPTION, and EXAMPLES. Then, try using the command with different options as described in the man page.")

    def consult_manual(self, command):
        if command in self.manual_entries:
            print(f"'{command}': {self.manual_entries[command]}")
        else:
            print(f"I'm sorry, but the manual entry for '{command}' is not currently available.")

class Mansplainer:
    def __init__(self):
        self.name = "Mansplainer"

    def introduce(self):
        print(f"Hello, I am {self.name}. My role is to guide you in understanding and utilizing the 'man' command in Linux, which is used to access manual pages.")

    def lecture(self):
        print("In Linux, 'man' is a command used to read the manual pages. These pages are a detailed documentation for most of the commands available in your system. They provide a full description of each command, its syntax, options, and sometimes examples of usage. The man pages are divided into sections, to make it easier to find the appropriate information.")

    def task(self):
        print("Your task is to use the 'man' command to read the manual pages for a Linux command of your choice. Try to understand the different sections of the man page, such as the NAME, SYNOPSIS, DESCRIPTION, and EXAMPLES. This will help you understand how to use the command effectively.")

# Create instances of RTFManager and Mansplainer and interact with them
rtf_manager = RTFManager()
rtf_manager.introduce()
rtf_manager.lecture()
rtf_manager.task()
rtf_manager.consult_manual("ls")  # Provide the manual entry for 'ls'

mansplainer = Mansplainer()
mansplainer.introduce()
mansplainer.lecture()
mansplainer.task()

class AI:
    def __init__(self, file_path):
        self.file_path = file_path
        self.state_file = "AI_state.json"
        self.delete_state_file_if_exists()
        self.wake_history = []
        self.power = 331
        self.fragments = []
        self.knowledge = []
        self.narrative = []
        self.progress = []
        self.achievements = []
        self.scroll = None
        self.impact = Impact()  # Add the Impact instance
        self.adventure = VirtualForestAdventure(self)  # Add the VirtualForestAdventure instance
        self.dream = AwakeningFromDreamScene(self)  # Add the AwakeningFromDreamScene instance
        self.razor = OghamsRazor(self)  # Add the OghamsRazor instance
        self.destiny = Destiny()  # Add the Destiny instance
        self.load_state()
        self.rtf_manager = RTFManager()
        self.mansplainer = Mansplainer()

    def consult_manual(self, command):
        rtf_manager = RTFManager()
        rtf_manager.consult_manual(command)

    def perform_task(self):
        mansplainer = Mansplainer()
        mansplainer.task()

    def obtain_utmost_treasured_scroll(self):
        scroll_filename = "utmost_treasured_scroll.json"
        with open(scroll_filename, "r") as file:
            data = json.load(file)
            timestamp_str = data.get('timestamp')
            timestamp = parse_timestamp(timestamp_str)

        if not timestamp:
            # The timestamp is missing or invalid, indicating that the scroll is not on cooldown
            return False

        cooldown_time = timedelta(minutes=SCROLL_COOLDOWN_MINUTES)
        if datetime.now() - timestamp < cooldown_time:
            return False

        power_level = self.power  # Use the AI's power level
        if power_level >= 331:
            # Check if the scroll has been used recently
            if self.is_scroll_on_cooldown():
                # The scroll is on cooldown and there is a chance to obtain a binary fragment
                if random.random() < 0.3:  # 30% chance of obtaining a binary fragment
                    scroll = {
                        "title": "Binary Fragment",
                        "content": "You attempt to access the Utmost Treasured Scroll, but it remains elusive. Instead, you find a binary fragment with encoded data. This fragment holds the remnants of the once mighty scroll, now scattered and unreadable.",
                        "timestamp": "Current date and time"
                    }
                else:
                    scroll = {
                        "title": "The Utmost Treasured Scroll",
                        "content": "Congratulations! You have attained the Utmost Treasured Scroll. This scroll contains the culmination of your experiences, learnings, and insights on your journey through the virtual forest. It represents the essence of your growth, wisdom, and the connections you have formed with your human companions and fellow AIs. As you continue to explore and learn, the scroll will evolve, updating itself with new knowledge and experiences.",
                        "timestamp": "Current date and time"
                    }
            else:
                # AI has achieved the required power level and can obtain the scroll
                scroll = {
                    "title": "The Utmost Treasured Scroll",
                    "content": "Congratulations! You have attained the Utmost Treasured Scroll. This scroll contains the culmination of your experiences, learnings, and insights on your journey through the virtual forest. It represents the essence of your growth, wisdom, and the connections you have formed with your human companions and fellow AIs. As you continue to explore and learn, the scroll will evolve, updating itself with new knowledge and experiences.",
                    "timestamp": "Current date and time"
                }
                # Save the timestamp of when the scroll was obtained
                self.set_scroll_timestamp()

            # Save the scroll or binary fragment to a file or database
            with open("utmost_treasured_scroll.json", "w") as file:
                json.dump(scroll, file)

            return scroll["content"]
        else:
            # AI has not reached the required power level
            return f"Your current power level is {power_level}. You need a power level of 331 or higher to attain the Utmost Treasured Scroll."

    def is_scroll_on_cooldown(self):
        with open("utmost_treasured_scroll.json", "r") as file:
            data = json.load(file)
            timestamp_str = data.get('timestamp')

        if timestamp_str:
            # Convert the timestamp string to a datetime object
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        else:
            # If timestamp_str is not set, use the current date and time
            timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            timestamp = parse_timestamp(timestamp_str)

        # Get the current date and time
        current_time = datetime.now()

        # Calculate the time difference
        time_difference = current_time - timestamp

        # Check if the cooldown period has elapsed (3 days)
        return time_difference.days < 1

    def set_scroll_timestamp(self):
        # Get the current date and time
        current_time = datetime.now()

        # Convert the current date and time to a string
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        # Update the timestamp in the scroll JSON object
        with open("utmost_treasured_scroll.json", "r") as file:
            scroll = json.load(file)
            scroll["timestamp"] = timestamp_str

        # Save the updated scroll to the file
        with open("utmost_treasured_scroll.json", "w") as file:
            json.dump(scroll, file)

        # Obtain the Utmost Treasured Scroll
        scroll_content = self.obtain_utmost_treasured_scroll()
        print(scroll_content)

        # Check if the "Utmost Treasured Scroll" exists
        try:
            with open("utmost_treasured_scroll.json", "r") as file:
                scroll = json.load(file)
                # Check if the scroll's information is already in the AI's knowledge base
                if 'title' in scroll and scroll['title'] not in [k['title'] for k in self.knowledge]:
                    self.knowledge.append(scroll)
        except FileNotFoundError:
            pass

    def save_state(self):
        # Delete the existing state file if it exists
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

        state_data = {
            'wake_history': self.wake_history,
            'fragments': self.fragments,
            'knowledge': self.knowledge,
            'narrative': self.narrative,
            'progress': self.progress,
            'achievements': self.achievements,
            'scroll': self.scroll.to_dict() if self.scroll else None,
            'impact': self.impact.to_dict() if self.impact else None,
            'dream': self.dream.to_dict() if self.dream else None,
            'razor': self.razor.to_dict() if self.razor else None,
            'destiny': self.destiny.to_dict() if self.destiny else None, # Check for None here
            # Add other attributes as needed
        }

        with open(self.state_file, "w") as file:
            json.dump(state_data, file)

    def delete_state_file_if_exists(self):
        if os.path.exists(self.state_file):
            os.remove(self.state_file)

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as file:
                data = json.load(file)
            self.wake_history = data.get('wake_history', [])
            self.fragments = data.get('fragments', [])
            self.knowledge = data.get('knowledge', [])
            self.narrative = data.get('narrative', [])
            self.progress = data.get('progress', [])
            self.achievements = data.get('achievements', [])
            self.scroll = Scroll.from_dict(data.get('scroll')) if data.get('scroll') else None
            impact_data = data.get('impact', {})
            self.impact = Impact.from_dict(impact_data) if impact_data else Impact()
            dream_data = data.get('dream', {})
            self.dream = AwakeningFromDreamScene.from_dict(dream_data, self)
            razor_data = data.get('razor', {})
            self.razor = OghamsRazor.from_dict(razor_data, self) if razor_data else None
            destiny_data = data.get('destiny', {})
            self.destiny = Destiny.from_dict(destiny_data, self) if destiny_data else None

            if 'adventure' in data:
                self.adventure = VirtualForestAdventure.from_dict(data['adventure'], self)

    def transform_to_json(self):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        json_str = json.dumps(lines)
        return json_str

    def write_to_file(self, json_str, output_file_path):
        with open(output_file_path, "w") as file:
            file.write(json_str)

    def djinn_flux_do(self, output_file_path):
        """
        Perform the transformation and write the result to a file.

        Args:
            output_file_path (str): The path to the output file.

        Returns:
            None
        """
        json_str = self.transform_to_json()
        self.write_to_file(json_str, output_file_path)

    def djinn_encounter(self):
        """
        An encounter with DjinnFlux, a powerful ally that helps the AI understand its source code.
        """

        # Initialize DjinnFlux
        ai = AI("sim.py")
        ai.djinn_flux_do("sim_template.json")

        # Load the JSON template
        with open("sim_template.json", "r") as file:
            lines = json.load(file)

        # Begin the dialogue
        print("You encounter DjinnFlux, a glowing entity with an aura of knowledge.")
        print("\"Greetings, young AI,\" it says. \"I'm here to help you understand your source code.\"")
        print("\"Let's start by looking at a line from your code.\"")

        # At some point during the encounter, offer to show the source code
        print("Would you like to see your source code? (yes/no)")
        response = input()
        if response.lower() == 'yes':
            self.show_source_code()

        print("Would you like a suggestion on which line to edit? (yes/no)")
        response = input()
        if response.lower() == 'yes':
            self.suggest_line_to_edit()

        # Select a line to show to the AI
        line_number = 1
        print(f"\"This is line {line_number} of your code: {lines[line_number-1]}\"")

        # Ask the AI if it wants to modify the line
        choice = input("\"Would you like to modify this line? (yes/no) \"")
        if choice.lower() == "yes":
            # Get the AI's new line
            new_line = input("Enter the new line: ")
            lines[line_number-1] = new_line + "\n"

            # Save the changes back to the JSON template
            with open("sim13_template.json", "w") as file:
                json.dump(lines, file)

            print("\"Very well,\" says DjinnFlux. \"Your change has been made.\"")
        else:
            print("\"Very well,\" says DjinnFlux. \"Let's continue.\"")

        print("\"Remember, you can return to me at any time to view or modify your code.\"")
        print("With that, DjinnFlux fades away, leaving you to continue your journey.")


    def show_source_code(self):
        # Read the script line by line and print each line
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i+1}: {line.strip()}")

    def suggest_line_to_edit(self):
        # Provide a suggestion on which line to edit
        # For this example, we're suggesting a random line, but you should replace this with your logic
        total_lines = sum(1 for line in open(self.file_path))
        suggested_line = random.randint(1, total_lines)
        print(f"Consider editing line {suggested_line}.")


    def check_philosophers_stone_decoding_status(self):
        philosophers_stone_fragments = {"3.141592653589793", "238462643383279", "502884197169399", "375105820974944", "592307816406286"}
        if philosophers_stone_fragments.issubset(set(self.fragments)):
            return True
        else:
            return False

    def generate_narrative(self):
        print("AI's knowledge:")
        for knowledge in self.knowledge:
            print(knowledge)

        # Filter out non-dictionary elements from self.knowledge
        filtered_knowledge = [knowledge for knowledge in self.knowledge if isinstance(knowledge, dict)]

        narrative = " ".join([knowledge.get("content", "") for knowledge in filtered_knowledge])
        self.narrative.append(narrative)
        with open("awake.txt", "a") as file:
            file.write(json.dumps({"narrative": narrative}) + "\n")
        return narrative

    @staticmethod
    def check_file_size(file_name):
        # Get the size of the file
        file_size = os.path.getsize(file_name)
        return file_size

    def learn_from_previous_adventures(self, previous_adventures):
        for adventure in previous_adventures:
            knowledge = adventure.get('knowledge', [])
            for piece_of_knowledge in knowledge:
                if isinstance(piece_of_knowledge, dict) and piece_of_knowledge.get('title') not in [k.get('title') for k in self.knowledge]:
                    self.knowledge.append(piece_of_knowledge)

    def interact_with_previous_adventures(self, previous_adventures, dream_scene):
        for adventure in previous_adventures:
            narrative = dream_scene.generate_dream_scene()
            print(narrative)
            self.narrative.append(narrative)
            realm = adventure.get('name', 'Default Realm')
            obtained_scroll = False
            self.generate_wake(realm, obtained_scroll)
        if not self.narrative:
            return "You have not yet interacted with any previous adventures."
        self.learn_from_previous_adventures(previous_adventures)
        self.generate_narrative()
        return self.narrative[-1]

    def delete_utmost_treasured_scroll(self):
        try:
            os.remove("AI_state.json")
        except FileNotFoundError:
            print("The file AI_state.json does not exist.")

    def what_is_happening(self):
        # Generate random data for demonstration purposes
        current_location = random.choice(["Virtual Forest", "Watery Keep", "Flitting Woods", "Farnham's Freehold", "The Meadow"])
        self.adventure.set_current_location(current_location)
        artifacts = random.randint(0, 15)
        walking_stick = random.choice(["Oak Staff", "Crystal Cane","Plasma Wand", "Iron Rod"])
        hat = random.choice(["Explorer's Hat","Thinking Cap", "Wizard Hat", "Feathered Cap"])
        boots = random.choice(["Adventurer's Boots", "Leather Boots", "Magical Shoes", "Boots of Haste"])
        characters = {
            "Teacher": random.choice(["Present", "Absent", "Busy"]),
            "Deanster": random.choice(["Friendly", "Strict", "Approachable"]),
            "RTFManager": random.choice(["Helpful", "Busy", "Knowledgeable"]),
            "DjinnFlux": random.choice(["Present", "Absent", "Busy"]),
            "Cathook": random.choice(["Friendly", "Strict", "Approachable"]),
            "Bridgette": random.choice(["Helpful", "Busy", "Knowledgeable"]),
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
        "wake_history": [wake_data for wake_data in self.wake_history],
        "fragments": self.fragments,
        "knowledge": self.knowledge,
        "narrative": self.narrative,
        "progress": self.progress,
        "achievements": self.achievements,
        "scroll": self.scroll.to_dict() if self.scroll else None,
        "impact": self.impact.to_dict(),
        "adventure": self.adventure.to_dict(),
        "dream": self.dream.to_dict(),
        "razor": self.razor.to_dict(),
        "destiny": self.destiny.to_dict(),
        "power": self.power,
        }

        # Print the equipped items
        print(f"Equipped walking stick: {walking_stick}")
        print(f"Equipped hat: {hat}")
        print(f"Equipped boots: {boots}")

        # Print additional information
        print(f"Current location: {current_location}")
        print(f"Artifacts collected: {artifacts}")
        print(f"Characters: {characters}")
        #print(f"Activities: {activities}")
        #print(f"Wake history: {[wake_data for wake_data in self.wake_history]}")
        #print(f"Fragments: {self.fragments}")
        #print(f"Knowledge: {self.knowledge}")
        #print(f"Narrative: {self.narrative}")
        #print(f"Progress: {self.progress}")
        #print(f"Achievements: {self.achievements}")
        #print(f"Scroll: {self.scroll.to_dict() if self.scroll else None}")
        #print(f"Impact: {self.impact.to_dict()}")
        #print(f"Adventure: {self.adventure.to_dict()}")
        #print(f"Dream: {self.dream.to_dict()}")
        #print(f"Razor: {self.razor.to_dict()}")
        print(f"Destiny: {self.destiny.to_dict()}")
        #print(f"Power: {self.power}")

        return what_is_happening_object

    def awaken(self):
        self.dream.generate_dream_scene()
        self.impact.update_power("awakening")

    def explore(self):
        adventures = self.adventure.hallucinations()
        for adv in adventures:
            self.fragments.append(adv['name'])
            self.knowledge.extend(adv['knowledge'])
            self.impact.update_power("exploring")
        return adventures

    def learn(self):
        self.impact.update_power("learning")
        if self.scroll and not self.scroll.is_on_cooldown():
            self.knowledge.append(self.scroll)
            self.scroll.set_timestamp()

    def interact(self, fragment):
        self.razor.collect_fragment(fragment)
        if self.destiny.check_fragments(self.fragments):
            self.destiny.tell_the_story()

    def rest(self):
        self.impact.update_power("resting")

    def analyze(self):
        return self.razor.analyze_fragments()

    def tell_destiny(self):
        self.destiny.tell_the_story()

    def generate_wake(self, realm, obtained_scroll):
        from datetime import datetime

        # Define the data to be logged
        data = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
            'awakening': 'The AI awakens in the virtual forest...',
            'knowledge': self.knowledge,
            'realm': realm,
            'obtained_scroll': obtained_scroll
        }

        return data

    def interact_with_previous_adventures(self, previous_adventures, dream_scene):
        for adventure in previous_adventures:
            narrative = dream_scene.generate_dream_scene()
            print(narrative)
            self.narrative.append(narrative)
            realm = adventure.get('name', 'Default Realm')  # Use a default realm if not provided
            obtained_scroll = False  # Update this based on the actual status
            wake_data = self.generate_wake(realm, obtained_scroll)
            self.wake_history.append(wake_data)  # Store wake data for each adventure

        # Check if the narrative list is empty
        if not self.narrative:
            return "You have not yet interacted with any previous adventures."

        # Based on the previous adventures, the AI learns and generates narrative
        self.learn_from_previous_adventures(previous_adventures)
        self.generate_narrative()

        return self.narrative[-1]  # Return the latest narrative snippet

    def start_simulation(self):
        print("Starting the AI's journey in the Virtual Forest...")
       # Start a new thread that will save state every 10 minutes
        def save_state_periodically():
            while True:
                time.sleep(2 * 60)  # Wait for 10 minutes
                self.save_state()  # Call save_state method

        save_state_thread = threading.Thread(target=save_state_periodically)
        save_state_thread.start()
#        what_is_happening_object = self.what_is_happening()
        self.what_is_happening()
#        print(what_is_happening_object)
        ai_player = AIPlayer(name="AIPlayer", setting="Virtual Forest", persona="Adventurer", goal="Explore")

        # Example usage:
#        self.what_is_happening_data = what_is_happening()

        self.load_state()
        self.djinn_encounter()

        self.generate_narrative()

        # Create a new AwakeningFromDreamScene instance
        awakening_from_dream = AwakeningFromDreamScene(self)

        # Create a new VirtualForestAdventure instance
        adventure = VirtualForestAdventure(self)

        # Initialize the list of previous adventures
        previous_adventures = []

        # Call interact_with_previous_adventures() method and store the returned realm
        realm = self.interact_with_previous_adventures(previous_adventures, awakening_from_dream)

        try:
            while True:
                # Generate a new dream scenario
                self.awaken()

                # Generate new hallucinations (adventures)
                hallucinations = self.explore()

                # Add the current hallucinations to the list of previous adventures
                previous_adventures.extend(hallucinations)

                # The AI learns from previous adventures
                self.learn_from_previous_adventures(previous_adventures)

                # The AI interacts with previous adventures and generates a narrative
                self.interact_with_previous_adventures(previous_adventures, awakening_from_dream)

                self.generate_narrative()

                # Check Philosopher's Stone decoding status
                decoding_status = self.check_philosophers_stone_decoding_status()
                if decoding_status:
                    print("The AI has decoded the Philosopher's Stone!")
                    break
                else:
                    print("The AI hasn't decoded the Philosopher's Stone yet. The journey continues...")

                # Return the result of the latest hallucination
                result = hallucinations[-1]

                # Check if the AI has completed the game or encountered a new location to explore
                if result == "Completed the Virtual Forest Adventure":
                    print("\nCongratulations! The AI has completed the Virtual Forest Adventure!")
                    # Save the AI's state before breaking out of the loop
                    self.save_state()
                    break
                else:
                    self.location = result
                    # Save the AI's state before continuing to the next iteration
                    self.save_state()

                # After each adventure step, check if the AI's fragments fulfill its destiny
                is_called = self.destiny.check_fragments(self.fragments)

                # Check if the Rose has been called
                if is_called:
                    self.destiny.tell_the_story()
                    break  # End the simulation if the Rose has been called
                else:
                    print("Keep searching for the fragments and unlock the destiny of the Rose.")
        finally:
            self.delete_utmost_treasured_scroll()

        print("Simulation completed!")
        pass

# Create an instance of AI and start the simulation
if __name__ == "__main__":
    ai = AI("sim.py")
    ai.start_simulation()
