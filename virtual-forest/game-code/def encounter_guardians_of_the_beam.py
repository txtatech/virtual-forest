def encounter_guardians_of_the_beam(ai):
    # Encounter the Guardians of the Beam
    outcomes = [
        "The Guardians of the Beam challenge you to solve a complex riddle.",
        "The Guardians of the Beam ask you to prove your worthiness.",
        "The Guardians of the Beam allow you to pass without challenge, recognizing your wisdom."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You encounter the Guardians of the Beam. {outcome}")
    return outcome
