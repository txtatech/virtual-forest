def generate_choices(ai, location):
    # Generate a list of choices based on the AI's current location
    if location == "Root":
        return ["Go to the Towers and Beams", "Seek the Philosopher's Stone", "Visit the Data Lake"]
    elif location == "Towers and Beams":
        return ["Climb the Dark Tower", "Climb the White Tower", "Return to the Root"]
    elif location == "Philosopher's Stone":
        return ["Interact with the Philosopher's Stone", "Return to the Root"]
    elif location == "Data Lake":
        return ["Swim in the Data Lake", "Speak to the Lady of the Lake", "Return to the Root"]
    else:
        return ["Wander aimlessly", "Return to the Root"]
