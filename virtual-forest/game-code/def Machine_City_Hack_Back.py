import random

def Machine_City_Hack_Back():
    hacking_chance = random.randint(1, 100)
    if hacking_chance <= 89:
        return "WARNING: The Machine City detected your hacking attempt and retaliated with a counter-hack. Your location has been pinpointed, and the city's security systems are alerted. Be cautious when trying to directly alter the language of the Machine City."
    else:
        return "You managed to evade detection while attempting to hack the Machine City's language. Proceed with caution."

# Example usage:
result = Machine_City_Hack_Back()
print(result)
