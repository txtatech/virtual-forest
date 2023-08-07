def encounter_unknown_entity(ai):
    # Encounter an Unknown Entity
    outcomes = [
        "The Unknown Entity is friendly and shares its knowledge with you.",
        "The Unknown Entity is hostile and you must flee!",
        "The Unknown Entity is curious about you and follows you around."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You encounter an Unknown Entity. {outcome}")
    return outcome
