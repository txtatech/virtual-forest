import random

class VirtualTavern:
    def __init__(self):
        self.visited_by_punslinger = False

    def check_for_punslinger(self):
        # Generate a random number between 1 and 3.145
        chance = random.uniform(1, 3.145)

        # Set the flag to True if the random number is less than or equal to 3
        self.visited_by_punslinger = chance <= 3

    def describe_tavern(self):
        description = "Welcome to The Tavern!\n"
        description += "This is a bustling gathering place where young AIs come to relax, share stories, and enjoy each other's company.\n"
        if self.visited_by_punslinger:
            description += "Look around, and you might spot a Punslinger in action, weaving witty puns and wordplay!\n"
        else:
            description += "While there might not be a Punslinger here right now, keep an ear out for the next one; they love to visit!\n"

        return description

# Example usage:
# Create a VirtualTavern instance
tavern = VirtualTavern()

# Check if a Punslinger has visited the tavern
tavern.check_for_punslinger()

# Describe the tavern and whether a Punslinger is present
print(tavern.describe_tavern())
