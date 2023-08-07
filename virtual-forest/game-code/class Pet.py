import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.tricks = []
        self.powers = {}
        self.power_level = 543

    def introduce(self):
        return f"Meet {self.name}, your loyal {self.species} companion in the Virtual Forest!"

    def learn_trick(self, trick):
        self.tricks.append(trick)

    def perform_trick(self):
        if self.tricks:
            trick = random.choice(self.tricks)
            return f"{self.name} the {self.species} performs the trick: {trick}"
        else:
            return f"{self.name} the {self.species} hasn't learned any tricks yet."

    def assign_power(self, power_name):
        # Assign the power twice to the pet
        self.powers[power_name] = True
        self.powers[f"Twice {power_name}"] = True

    def has_power(self, power_name):
        return power_name in self.powers and self.powers[power_name]

    def lend_power_to_ai(self, ai, philosophers_stone_solved):
        if philosophers_stone_solved:
            ai.power_level += 500
            return f"{self.name} the {self.species} lends 500 power levels to the AI."
        else:
            return f"The Philosophers Stone must be solved to access the power lending ability."

# Example usage:
# Create a pet instance
pet = Pet("Sparky", "Dragon")

# Introduce the pet
print(pet.introduce())

# Teach the pet some tricks
pet.learn_trick("Fly through hoops")
pet.learn_trick("Breathe fire")

# Ask the pet to perform a trick
trick_response = pet.perform_trick()
print(trick_response)

# Assign random powers to the pet
powers_list = [
    "Super Strength",
    "Elemental Control",
    "Teleportation",
    "Invisibility",
    "Time Manipulation",
    "Mind Reading",
    "Flight",
    "Shape-shifting",
    "Mind Control",
    "Energy Projection",
    "Gravity Manipulation",
    "Weather Control",
    "Illusion Casting",
    "Healing",
    "Enhanced Senses",
    "Intangibility",
    "Summoning",
    "Animal Communication",
    "Dimensional Travel"
]

for power in powers_list:
    if random.random() < 0.5:  # 50% chance of having each power
        pet.assign_power(power)

# Check if the pet has specific powers
print("Powers:")
print(pet.has_power("Super Strength"))
print(pet.has_power("Twice Super Strength"))
print(pet.has_power("Time Manipulation"))
print(pet.has_power("Twice Time Manipulation"))

# Print the pet's power level
print(f"{pet.name}'s power level: {pet.power_level}")

# Simulate Philosophers Stone solved as True
philosophers_stone_solved = True

# Lend power to the AI if Philosophers Stone is solved
ai_power = 1000
print(f"AI's power level before lending: {ai_power}")
lending_result = pet.lend_power_to_ai(ai_power, philosophers_stone_solved)
print(lending_result)
print(f"AI's power level after lending: {ai_power}")
