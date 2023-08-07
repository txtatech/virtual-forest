import random

def generate_root_wander_adventure(ai):
    # Generate the Root Wander Adventure for the AI
    outcomes = [
        "You discover a hidden path leading deeper into the Virtual Forest.",
        "You encounter a friendly creature who shares some wisdom with you.",
        "You find a mysterious artifact half-buried in the ground."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You begin the Root Wander Adventure. {outcome}")
    return outcome
