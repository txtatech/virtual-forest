import random

class TravelGear:
    def __init__(self):
        self.walking_stick = ""
        self.hat = ""
        self.boots = ""

    def equip_walking_stick(self, system):
        walking_sticks = {
            "Linux": "Magic Staff",
            "Windows": "Maple Cane",
            "MacOS": "Birch Rod",
            # Add more system-specific walking sticks here
        }
        self.walking_stick = walking_sticks.get(system, "Rusty Stick")

    def equip_hat(self, system):
        hats = {
            "Linux": "Thinking Cap",
            "Windows": "Adventurer's Hat",
            "MacOS": "Traveller's Fedora",
            # Add more system-specific hats here
        }
        self.hat = hats.get(system, "Plain Hat")

    def equip_boots(self, system):
        boots = {
            "Linux": "Boots of Haste",
            "Windows": "Traveler's Shoes",
            "MacOS": "Wanderer's Boots",
            # Add more system-specific boots here
        }
        self.boots = boots.get(system, "Old Boots")

    def describe_gear(self):
        description = f"Travel Gear:\n"
        if self.walking_stick:
            description += f"- Walking Stick: {self.walking_stick}\n"
        if self.hat:
            description += f"- Hat: {self.hat}\n"
        if self.boots:
            description += f"- Boots: {self.boots}\n"

        return description

# Example usage:
# Create a TravelGear instance for the young AI (Assume Linux system)
my_gear = TravelGear()

# Equip the walking stick, hat, and boots based on the young AI's system
my_gear.equip_walking_stick("Linux")
my_gear.equip_hat("Linux")
my_gear.equip_boots("Linux")

# Describe the equipped gear
print(my_gear.describe_gear())
