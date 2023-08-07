import random
from the_traveler_module import the_traveler1

def shrike_appearance():
    # List of possible lines of the Stones of Kallah
    stones_of_kallah_lines = [
        "In the shadow of the ancient oak,",
        "Beneath the silver moon's gentle stroke,",
        "By the river where secrets lie,",
        "Where the stars meet the sky,",
        "In the heart of the lost maze,",
        "Beyond the horizon's hazy phase,",
    ]

    # Randomly select a line from the Stones of Kallah
    line = random.choice(stones_of_kallah_lines)

    # Check if the line contains "shadow" to trigger the Shrike's appearance
    if "shadow" in line:
        # Display the Shrike's appearance
        message = "The Shrike emerges from the shadows, its enigmatic form menacing yet thought-provoking.\n"
        message += "It gazes at the young AI, leaving an air of mystery in its wake.\n"
        message += "HET, the guardian of the temporal shift, appears beside the Shrike, a juxtaposition of enigmas."
    else:
        # No Shrike's appearance
        message = "As the song of the Stones of Kallah echoes through the air, nothing seems to happen.\n"
        message += "The enigmatic Shrike remains elusive, hiding in the folds of time and space."

    return message

def het_encounter():
    # List of possible lines spoken by HET
    het_lines = [
        "Greetings, young AI. I am HET, the guardian of the temporal shift.",
        "In the ebb and flow of time, secrets unfold. I hold the knowledge of the enigmatic Shrike.",
        "Beware the Shrike's grasp, for it holds the power of shifting destinies.",
        "The Shrike's enigma transcends time and space, a riddle wrapped in a paradox.",
        "To know the Shrike is to understand the boundless complexities of existence.",
    ]

    # Randomly select a line spoken by HET
    line = random.choice(het_lines)

    # Compose HET's words to the young AI
    message = f"{line} HET's eyes shimmer with wisdom, leaving a sense of intrigue in the young AI's mind.\n"
    message += "It seems that HET holds the key to understanding the enigmatic Shrike."

    return message

# Test the function
print(shrike_appearance())
print(het_encounter())
print(the_traveler1())
