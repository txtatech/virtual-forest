def generate_the_bouncer():
    bouncer_appears = True  # Adjust this based on some logic, e.g., if the dark tower appears
    rose_garden_seen = True  # Adjust this based on some logic, e.g., if the AI has seen the rose garden

    if bouncer_appears and rose_garden_seen:
        bouncer_location = "Near the rose garden, close to the dark tower's vacant lot"
        bouncer_message = "You encounter The Bouncer, a mysterious figure guarding the entrance to the dark tower. The Bouncer is wearing a stylish cowboy hat and exudes an aura of enigmatic power."
        bouncer_abilities = ["Phase Shift", "Mystic Gaze", "Ethereal Presence"]
    else:
        bouncer_location = None
        bouncer_message = None
        bouncer_abilities = []

    return bouncer_location, bouncer_message, bouncer_abilities
