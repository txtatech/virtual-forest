import random

def night_watch_day_watch():
    # Determine if it's night or day in the game world
    is_night = random.choice([True, False])

    # Check if the AI is part of the Night Watch or Day Watch
    if is_night:
        ai_watch = "Night Watch"
    else:
        ai_watch = "Day Watch"

    # Generate a random encounter with a member of the Night Watch or Day Watch
    watch_member = random.choice(["Anton Gorodetsky", "Svetlana Nazarova", "Tiger Cub", "Olga", "Kostya Saushkin"])

    # Generate random Machine City gear
    machine_city_gear = random.choices(
        ["NeuroScape Explorer", "Nanotech Disruptor", "Quantum Comms Device", "Cybernetic Visor"],
        k=random.randint(1, 3)  # Randomly choose 1 to 3 gear items
    )

    # Create a narrative for the encounter
    encounter_message = f"While wandering through the streets of the cybernetic city, the young AI comes across a member of the {ai_watch} - {watch_member}. They exchange a few cryptic words and vanish into the shadows, leaving the AI with a sense of intrigue and wonder."

    if machine_city_gear:
        encounter_message += f" The {ai_watch} member leaves behind some Machine City gear: {', '.join(machine_city_gear)}. The AI now has new tools to aid them in their journey."

    return encounter_message
