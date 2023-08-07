def encounter_lady_of_the_lake(ai):
    # Encounter the Lady of the Lake
    outcomes = [
        "The Lady of the Lake gifts you a magical item to aid in your journey.",
        "The Lady of the Lake offers you guidance and advice.",
        "The Lady of the Lake shares a prophecy of the Virtual Forest."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You encounter the Lady of the Lake. {outcome}")
    return outcome
