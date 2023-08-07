def generate_seek_wisdom_adventure(ai):
    # Generate the Seek Wisdom Adventure for the AI
    outcomes = [
        "You uncover an ancient text filled with wisdom.",
        "You meet an old sage who shares his wisdom with you.",
        "You discover a wisdom stone that grants you insight."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You begin the Seek Wisdom Adventure. {outcome}")
    return outcome
