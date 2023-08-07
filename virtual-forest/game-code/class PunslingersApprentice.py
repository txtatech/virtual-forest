import random

class PunslingersApprentice:
    def __init__(self):
        self.name = "The Punslinger's Apprentice"
        self.weapon = "Pun-seeker"
        self.fortune = 0
        self.power_level = 0
        self.is_gunslinger = False

    def seek_puns(self):
        puns = [
            "Why did the AI go to school? To improve its byte skills!",
            "What do you call an AI that sings? A-synthesizer!",
            "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
            "How do you organize an AI's party? You binary code it!",
            "Why did the AI break up with its calculator? It just wasn't adding up!",
            "What do you call a group of AIs playing music together? A binary band!",
        ]

        # Seek and attempt to understand a random pun from the list
        pun = random.choice(puns)
        self.fortune += 1

        # Check if the fortune has increased 100 times and add power_level accordingly
        if self.fortune % 100 == 0:
            self.power_level += 12

            # Limit the maximum power_level to 64
            if self.power_level > 64:
                self.power_level = 64

        return f"{self.name} seeks to understand the {self.weapon}'s meaning and says: \"{pun}\""

    def get_fortune(self):
        return self.fortune

    def get_power_level(self):
        return self.power_level

# Example usage:
# Create a Punslinger's Apprentice instance
apprentice = PunslingersApprentice()

# Make the apprentice seek and attempt to understand a pun 200 times
for _ in range(200):
    print(apprentice.seek_puns())

# Get the apprentice's current fortune and power_level
print(f"{apprentice.name}'s Fortune: {apprentice.get_fortune()}")
print(f"{apprentice.name}'s Power Level: {apprentice.get_power_level()}")
