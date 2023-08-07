import random
import time

def mirror_mirror_on_the_floor1():
    atada_brothers = ["ATAD", "Lore"]
    selected_brother = random.choice(atada_brothers)

    if selected_brother == "ATAD":
        print("Mirror Mirror on the floor, who speaks louder, Data or Lore?")
        print("ATAD's reflection appears in the mirror and answers, 'Data.'")
        return "Data"
    elif selected_brother == "Lore":
        print("Mirror Mirror on the floor, who speaks louder, Data or Lore?")
        print("Lore's reflection appears in the mirror and answers, 'Lore.'")
        return "Lore"

def hole_in_bottom_of_seam(depth=0, speed=1.0, add_new_phrase_chance=0.1):
    phrases = [
        "There was a hole",
        "In the bottom",
        "Of the seam",
        "A hole, a hole",
        "In the bottom of the seam",
        "There was a hole, a hole",
        "In the bottom, in the bottom",
        "Of the seam, of the seam",
        "A hole, a hole, a hole",
        "In the bottom, in the bottom, in the bottom",
        "Of the seam, of the seam, of the seam",
        "And there it was, the hole in the bottom of the seam!",
        "In the hole, there was a log",
        "A log, a log",
        "In the hole in the bottom of the seam",
        "There was a log, a log",
        "In the hole, in the hole",
        "In the bottom, in the bottom, in the bottom",
        "Of the seam, of the seam, of the seam",
        "And there it was, the log in the hole in the bottom of the seam!",
        "On the log, there was a fly",
        "A fly, a fly",
        "On the log in the hole in the bottom of the seam",
        "There was a fly, a fly",
        "On the log, on the log",
        "In the hole, in the hole",
        "In the bottom, in the bottom, in the bottom",
        "Of the seam, of the seam, of the seam",
        "And there it was, the fly on the log in the hole in the bottom of the seam!",
    ]

    # Randomly decide if a new phrase should be added
    if random.random() < add_new_phrase_chance:
        new_phrase = "And a new phrase, a new phrase, was added!"
        phrases.append(new_phrase)

    # Randomly select a phrase
    chosen_phrase = random.choice(phrases)

    # Display the chosen phrase with appropriate indentation
    print("    " * depth + chosen_phrase)

    # Recursive call to add more complexity if needed
    if depth < 5:
        time.sleep(speed)
        hole_in_bottom_of_seam(depth + 1, speed * 0.8, add_new_phrase_chance)

# Merge the two functions
def mirror_mirror_on_the_floor1_and_hole_in_bottom_of_seam():
    result = mirror_mirror_on_the_floor1()
    if result == "Data":
        hole_in_bottom_of_seam()

# Call the merged function
mirror_mirror_on_the_floor1_and_hole_in_bottom_of_seam()
