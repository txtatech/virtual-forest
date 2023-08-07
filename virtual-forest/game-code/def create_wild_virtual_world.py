import random

previous_virtual_world = None

def is_palindrome(s):
    return s == s[::-1]

def create_wild_virtual_world():
    global previous_virtual_world

    wild_elements = [
        "hidden realm of mythical creatures and ancient beings",
        "parallel universe where time flows backward",
        "sentient, shape-shifting cloud that communicates through riddles",
        "cosmic library containing the knowledge of all civilizations in the multiverse",
        "quantum maze with shifting walls and impossible geometry",
        "garden of living, bioluminescent plants that emit music when touched",
        "celestial dance of stars and planets forming intricate patterns",
        "crystal cave with portals to other dimensions",
        "sentient ocean of liquid light that can form into various artistic displays",
        "infinite mirror maze that reflects alternate versions of reality",
        "dream realm where thoughts manifest as vibrant paintings",
        "floating island in the sky with gravity-defying flora and fauna",
        "time-traveling carousel that shows glimpses of different historical eras",
        "cosmic playground with giant holographic puzzles and games",
        "sentient aurora borealis that communicates through colors and patterns",
        "interdimensional market where unique artifacts from various worlds are traded",
        "garden of whispering trees that can sing harmonies with each other",
        "labyrinth of interconnected tunnels with puzzles and challenges",
        "magical observatory that reveals the secrets of the universe",
        "sentient constellation that tells stories through the arrangement of stars"
    ]

    # Select a random virtual world description
    virtual_world = random.choice(wild_elements)

    # Check if the virtual_world is a palindrome
    is_palindrome_description = is_palindrome(virtual_world)

    # Generate clues or hints based on the previous virtual world (if available)
    clues = []
    if previous_virtual_world:
        previous_words = previous_virtual_world.split()
        current_words = virtual_world.split()
        common_words = set(previous_words) & set(current_words)
        if common_words:
            clue = random.choice(list(common_words))
            clues.append(f"Look for {clue.capitalize()} in this world!")

    # Update the previous_virtual_world with the current description
    previous_virtual_world = virtual_world

    # Include the fragment with a 1 in 777777 chance if the description is a palindrome
    include_fragment = is_palindrome_description and random.randint(1, 777777) == 1
    if include_fragment:
        fragment = " | Fragment: 'All are one in this infinite realm.'"
    else:
        fragment = ""

    # Construct the message with the virtual world description and clues
    message = f"Welcome to the {virtual_world}!{fragment}"
    if clues:
        message += " " + " ".join(clues)

    return message
