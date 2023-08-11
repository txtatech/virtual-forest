import time
import random
import nltk
from nltk.chat.util import Chat, reflections
import json

class CaraCode:
    def __init__(self):
        self.cara_filename = "Cara.py"
        self.json_filename = "cara_content.json"

    def read_cara_content(self):
        try:
            with open(self.cara_filename, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"{self.cara_filename} not found. Please make sure the file exists.")
            return None

    def write_json_file(self, content):
        data = {
            "cara_content": content
        }
        with open(self.json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def generate_code(self, filename="Cara", num_random_entries=5):
        # Read the content of the Cara.py file
        cara_content = self.read_cara_content()
        if cara_content is None:
            return

        # Save the Cara.py content to a JSON file
        self.write_json_file(cara_content)

        # Generate random question-answer pairs
        random_entries = []
        for _ in range(num_random_entries):
            random_question = "Random Question"
            random_answer = f"Random Answer {_}"
            random_entries.append((random_question, [random_answer]))

        # Generate the new code using the stored content and random entries
        new_code = f'''
{cara_content}

# Add random question-answer pairs
pairs.extend({random_entries})

# Create an instance of NewCara
new_cara = NewCara()

# Optionally, you can add additional question-answer pairs
new_cara.add_question_answer("what's your name?", '"My name is Cara."')

# Generate the code and save it to a file
new_cara.generate_code()
'''

        # Write the new code to a Python file
        timestamp = time.strftime("_%Y%m%d_%H%M%S")
        full_filename = f"{filename}{timestamp}.py"
        with open(full_filename, 'w') as file:
            file.write(new_code)

# Create an instance of CaraCode
code_generator = CaraCode()

# Generate the code and save it to a file
code_generator.generate_code(num_random_entries=10)  # Example: Generate 10 random entries
