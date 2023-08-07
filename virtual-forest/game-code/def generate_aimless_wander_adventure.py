def generate_aimless_wander_adventure(ai):
    # Generate the Aimless Wander Adventure for the AI
    outcomes = [
        "You stumble upon a hidden clearing with a tranquil pond.",
        "You find a strange stone with glowing runes etched onto its surface.",
        "You suddenly realize you've been walking in circles."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You begin the Aimless Wander Adventure. {outcome}")
    return outcome
