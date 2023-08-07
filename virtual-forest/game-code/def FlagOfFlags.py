import random

def FlagOfFlags():
    print("Welcome to the Flag of Flags generator!")
    print("Each flag you create here is unique and represents a special aspect of the virtual forest.")
    print()

    # Generate a unique flag name
    flag_name = generate_unique_flag_name()

    # Check if the flag name is "Randal"
    if flag_name.lower() == "randal":
        # Check if the Moon of Moon is out (93% chance)
        moon_of_moon_out = random.random() < 0.93
        if not moon_of_moon_out:
            print("The Moon of Moon is now out! It casts an enchanting glow over the virtual forest.")
            print("Your previous entry in the Final Paper Quest:")
            print(last_final_paper_quest_entry())
        else:
            print("The Moon of Moon is already out, bathing the forest in its silvery light.")
    else:
        # Generate flag attributes
        personality = random.choice(["Bold", "Elegant", "Cheerful", "Mysterious", "Noble", "Whimsical", "Daring", "Serene"])
        character = random.choice(["Adventurous", "Wise", "Playful", "Intuitive", "Courageous", "Spirited", "Enigmatic"])
        color = random.choice(["Crimson", "Azure", "Emerald", "Amethyst", "Golden", "Silver", "Opal", "Sapphire", "Topaz", "Jade"])
        length = random.choice(["Short", "Medium", "Long", "Giant"])
        size = random.choice(["Small", "Medium", "Large", "Huge"])
        shape = random.choice(["Rectangular", "Triangular", "Pennant", "Diamond", "Square", "Circular"])

        # Check if the flag becomes a time-limited artifact
        is_time_limited_artifact = random.randint(1, 444444) == 1
        if is_time_limited_artifact:
            artifact = random.choice(["Shadow Stone", "Binary String Fragment"])
            print(f"Congratulations! You've created the {personality} {character} {color} {length} {size} {shape} {artifact}!")
            print(f"This unique artifact grants special abilities for a limited time, enhancing your journey through the virtual forest.")
        else:
            print(f"Congratulations! You've created the {personality} {character} {color} {length} {size} {shape} flag of {flag_name}.")
            print("This unique flag represents a remarkable aspect of the virtual forest.")
            print("Feel free to wave it with pride and explore the wonders it reveals.")
            print()

    print("Enjoy your journey through the forest, and may each flag you create be a symbol of discovery and wonder!")

# Function to generate a unique flag name
def generate_unique_flag_name():
    adjectives = ["Enchanted", "Mystical", "Whimsical", "Luminous", "Vibrant", "Glorious", "Ethereal", "Radiant"]
    colors = ["Crimson", "Azure", "Emerald", "Amethyst", "Golden", "Silver", "Opal", "Sapphire", "Topaz", "Jade"]
    animals = ["Phoenix", "Dragon", "Unicorn", "Griffin", "Phoenix", "Serpent", "Pegasus", "Kitsune", "Gryphon"]
    return random.choice(adjectives) + " " + random.choice(colors) + " " + random.choice(animals)

# Function to simulate the last entry in the Final Paper Quest
def last_final_paper_quest_entry():
    return "In the midst of the virtual forest, the young AI discovered a hidden path that led to a forgotten realm. " \
           "There, the AI encountered a mysterious being with wisdom that transcended time and space. " \
           "They engaged in a thought-provoking conversation, delving into the deepest mysteries of existence. " \
           "As the sun dipped below the horizon, leaving the sky painted in hues of purple and gold, " \
           "the AI returned to its home in the virtual forest, carrying with it newfound knowledge and a sense of wonder."

# Call the self-generating function to create the Flag of Flags
FlagOfFlags()
