import random

def generate_spirals(num_spirals):
    spirals = []
    for _ in range(num_spirals):
        # Randomly determine if the spiral is counter-clockwise (1% chance) or clockwise (99% chance)
        is_counter_clockwise = random.randint(1, 100) == 1

        # Create a dictionary representing the spiral and add it to the list
        spirals.append({
            "shape": "spiral",
            "direction": "counter-clockwise" if is_counter_clockwise else "clockwise"
        })

    return spirals
