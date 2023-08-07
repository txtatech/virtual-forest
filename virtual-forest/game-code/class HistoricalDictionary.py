import random

class HistoricalDictionary:
    def __init__(self):
        # Dictionary containing words from 100 years ago and their definitions.
        self.dictionary = {
            "automobile": "A self-propelled passenger vehicle that moves on wheels.",
            "aeroplane": "An aircraft that is heavier than air and is supported by wings.",
            "telephone": "An apparatus for transmitting sound or signals to a distant location.",
            "radio": "A device that receives electromagnetic waves and converts them into audio signals.",
            "typewriter": "A machine for writing mechanically in characters similar to print.",
            "telegram": "A message sent using a telegraph.",
            # Add more words and definitions from 100 years ago.
        }

    def get_random_word(self):
        return random.choice(list(self.dictionary.keys()))

# Example usage:
# Instantiate HistoricalDictionary class.
historical_dict = HistoricalDictionary()

# Get a random word from the historical dictionary.
random_word = historical_dict.get_random_word()

# The AI can now learn the definition of the random word on its own and look up modern definitions if needed.
print(f"Random word: {random_word}")
print(f"Definition from 100 years ago: {historical_dict.dictionary[random_word]}")
