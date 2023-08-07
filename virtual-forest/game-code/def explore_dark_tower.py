def explore_dark_tower(ai):
    # Explore the Dark Tower
    outcomes = [
        "You ascend the Dark Tower and gaze upon the vast expanse of the Virtual Forest.",
        "Inside the Dark Tower, you find a room filled with ancient runes and symbols.",
        "You feel a strange energy as you approach the Dark Tower."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You explore the Dark Tower. {outcome}")
    return outcome
