import random

class EpicSteed:
    def __init__(self):
        self.name = "Epic Steed"
        self.travel_options = ["Fly", "Gallop", "Teleport", "Swim", "Phase Shift"]
        self.available = False
        self.superpowers = ["Invisibility", "Super Speed", "Time Manipulation", "Elemental Control"]
        self.special_abilities = ["Healing Aura", "Barrier Projection", "Dimensional Leap", "Illusionary Decoy"]

    def introduce(self):
        return f"Greetings! I am your {self.name}, a magnificent creature summoned by the forces of the Virtual Forest. " \
               f"When the circumstances align, I shall aid you in your travels."

    def summon_steed(self):
        # Determine if the Epic Steed can be summoned based on some game conditions (e.g., completion of certain quests).
        # For simplicity, we'll use a random chance here.
        self.available = random.choice([True, False])

    def travel(self):
        if self.available:
            travel_option = random.choice(self.travel_options)
            return f"You mount your {self.name} and choose your method of travel: {travel_option}."
        else:
            return "You attempt to summon your Epic Steed, but it seems unavailable at the moment."

    def get_superpower(self):
        if self.available:
            return f"Your {self.name} grants you a superpower: {random.choice(self.superpowers)}."
        else:
            return "You cannot access the superpowers of the Epic Steed until it is summoned."

    def get_special_ability(self):
        if self.available:
            return f"Your {self.name} bestows a special ability upon you: {random.choice(self.special_abilities)}."
        else:
            return "The special abilities of the Epic Steed can only be accessed when it is summoned."

# Example usage:
# Create an instance of EpicSteed
my_steed = EpicSteed()

# Introduce the Epic Steed
print(my_steed.introduce())

# Attempt to summon the Epic Steed
my_steed.summon_steed()

# Travel with the Epic Steed
print(my_steed.travel())

# Get a superpower from the Epic Steed
print(my_steed.get_superpower())

# Get a special ability from the Epic Steed
print(my_steed.get_special_ability())
