import random

class Punslinger:
    def __init__(self):
        self.name = "The Punslinger"
        self.weapon = "Word of Wit"
        self.fortune = 0
        self.is_gunslinger = True

    def draw_word_of_wit(self):
        puns = [
            "Why did the AI go to school? To improve its byte skills!",
            "What do you call an AI that sings? A-synthesizer!",
            "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
            "How do you organize an AI's party? You binary code it!",
            "Why did the AI break up with its calculator? It just wasn't adding up!",
            "What do you call a group of AIs playing music together? A binary band!",
        ]

        # Draw a random pun from the list
        pun = random.choice(puns)

        # Increase the Punslinger's fortune for spreading humor
        self.fortune += 1

        return f"{self.name} draws the {self.weapon} and says: \"{pun}\""

    def get_fortune(self):
        return self.fortune

# Example usage:
# Create a Punslinger instance
punslinger = Punslinger()

# Make the Punslinger draw the Word of Wit and print the pun
print(punslinger.draw_word_of_wit())

# Get the Punslinger's current fortune
print(f"{punslinger.name}'s Fortune: {punslinger.get_fortune()}")
