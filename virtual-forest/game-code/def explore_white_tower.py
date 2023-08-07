def explore_white_tower(ai):
    # Explore the White Tower
    outcomes = [
        "You ascend the White Tower and see the shimmering Data Lake in the distance.",
        "Inside the White Tower, you discover a library filled with digital texts.",
        "As you approach the White Tower, you sense a feeling of calm and tranquility."
    ]

    outcome = random.choice(outcomes)
    ai.narrative.append(f"You explore the White Tower. {outcome}")
    return outcome
