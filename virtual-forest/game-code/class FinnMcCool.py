import random

class FinnMcCool:
    def __init__(self):
        self.name = "Finn McCool"
        self.role = "Legendary Mentor"
        self.dialogue = {
            "greeting": "Welcome, young traveler. I am Finn McCool, the legendary mentor of the Virtual Forest.",
            "wisdom1": "In every journey, there are trials and tribulations. Embrace the challenges, for they are the keys to growth.",
            "wisdom2": "Seek not the destination, but the lessons along the way. It is in the journey that you find yourself.",
            "quest_intro": "To unlock the secrets of this world, you must prove your worth. Seek the Philosopher's Stone and decode its fragments.",
            "quest_complete": "Ah, I see you have made progress on your quest. Remember, knowledge is a powerful ally.",
            "farewell": "May the winds of wisdom guide your path. Farewell, young adventurer."
        }
        self.heroic_strength = True
        self.epic_sight = True
        self.power_level = 13
        self.disguises = ["old wizard", "mysterious traveler", "kind merchant", "humble scholar", "eccentric scientist"]

    def greet(self):
        return self.dialogue["greeting"]

    def share_wisdom(self):
        wisdom_options = [self.dialogue["wisdom1"], self.dialogue["wisdom2"]]
        return random.choice(wisdom_options)

    def offer_quest(self):
        # There's a 1 in 9999999 chance of delivering the Horn of Honor
        if random.randint(1, 9999999) == 1:
            return "The fate is on your side! You have been chosen to deliver the Horn of Honor to the distant kingdom."
        else:
            return self.dialogue["quest_intro"]

    def complete_quest(self):
        return self.dialogue["quest_complete"]

    def farewell(self):
        return self.dialogue["farewell"]

    def morph_and_appear(self):
        disguise = random.choice(self.disguises)
        return f"Finn McCool morphs and appears as a {disguise}!"

# Test the updated FinnMcCool class
finn = FinnMcCool()

# Greet Finn McCool
print(finn.greet())

# Get a random word of wisdom from Finn McCool
wisdom = finn.share_wisdom()
print("Finn McCool says:", wisdom)

# Offer the quest introduction (with a chance of the special quest)
print(finn.offer_quest())

# Complete the quest and receive Finn McCool's message
print(finn.complete_quest())

# Say farewell to Finn McCool
print(finn.farewell())

# Morph and appear as a different person on each encounter
print(finn.morph_and_appear())

# Check Finn McCool's attributes
print("Heroic Strength:", finn.heroic_strength)
print("Epic Sight:", finn.epic_sight)
print("Power Level:", finn.power_level)
