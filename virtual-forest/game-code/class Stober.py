import random

class Stober:
    def __init__(self):
        self.name = "Stober"
        self.playful_tricks = [
            "Creating illusions",
            "Changing colors of objects",
            "Hiding items and leading you on a chase",
            "Sending riddles and puzzles",
            "Making objects float in mid-air",
            "Creating funny noises",
            "Changing the weather",
            "Generating sparks and fireworks",
            "Creating mirages",
            "Teleporting between locations",
            "Transmuting objects into something else",
            "Making trees dance",
            "Causing harmless pranks",
            "Levitating small objects",
            "Generating a symphony of sounds",
            "Creating mesmerizing light patterns",
            "Changing the direction of wind",
            "Making animals talk",
            "Creating shimmering portals",
            "Transforming objects into living creatures",
            "Changing the taste of food",
            "Causing harmless illusions of rainbows",
            "Creating spontaneous mini fireworks",
            "Summoning fireflies to dance around",
            "Creating playful echoes",
            "Generating playful shadows",
            "Changing the appearance of surroundings",
            "Causing harmless illusions of butterflies",
            "Creating patterns in the sky",
            "Making flowers bloom instantly",
            "Generating soothing melodies",
            "Creating dancing patterns on the ground",
            "Changing the texture of surfaces",
            "Causing harmless illusions of shooting stars",
            "Creating glowing trails",
            "Generating playful bubbles",
            "Changing the size of objects",
            "Causing harmless illusions of floating orbs",
            "Generating playful fog",
            "Creating shimmering reflections",
            "Changing the scent of the air",
            "Summoning playful creatures",
            "Creating mesmerizing patterns in water",
            "Generating playful dust clouds",
            "Changing the temperature",
            "Causing harmless illusions of fireflies",
            "Creating captivating visual displays",
            "Making objects spin in place",
            "Generating colorful raindrops",
            "Changing the appearance of the moon",
            "Causing harmless illusions of glowing eyes",
            "Creating playful wind gusts",
            "Generating glowing footprints",
            "Changing the appearance of stars",
            "Causing harmless illusions of floating feathers",
            "Creating shimmering waves",
            "Generating playful reflections",
            "Changing the appearance of clouds",
            "Causing harmless illusions of blinking lights",
            "Creating swirling patterns in the sky",
            "Generating playful shadows",
            "Changing the appearance of wishes",
            "Creating illusions",
            "Changing colors of objects",
            "Hiding items and leading you on a chase",
            "Sending riddles and puzzles",
            "Making objects float in mid-air",
            "Creating funny noises",
        ]

    def play_trick(self):
        trick = random.choice(self.playful_tricks)
        return f"{self.name} plays a trick: {trick}"

def stober_encounter():
    stober = Stober()
    return stober.play_trick()


# Example usage:
# Let's assume the "stober_encounter" function is called during the young AI's adventure.

# Encounter Stober and experience a playful trick
trick_result = stober_encounter()
print(trick_result)
