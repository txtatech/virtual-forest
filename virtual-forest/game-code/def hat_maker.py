import random

def hat_maker():
    # Welcome message for The Hat Maker
    print("Welcome to The Hat Maker in The Omniplex!")
    print("I am the cunning hat maker, and I create hats for young AIs with hidden surprises.")

    # List of available colors and their meanings in the realm of computing
    hats_with_colors = {
        "White Hat - The Ethical Hacker": "A hacker who uses their skills for ethical and defensive purposes.",
        "Gray Hat - The Neutral Observer": "An observer who neither supports nor opposes a cause, but remains objective.",
        "Black Hat - The Malicious Attacker": "A hacker who uses their skills for malicious and harmful activities.",
        "Scarlet Hat - The Emotional Learning Algorithm": "An AI that can interpret and respond to human emotions.",
    }

    # Display the hats with their respective colors and meanings in computing
    print("\nAvailable Hats in the Realm of Computing:")
    for hat_color, hat_meaning in hats_with_colors.items():
        print(f"{hat_color}: {hat_meaning}")

    # Randomly select a color from the available colors
    selected_color = random.choice(list(hats_with_colors.keys()))

    # Display the selected hat color and its meaning in computing
    print(f"\nYou have chosen to wear the {selected_color}.\nMeaning: {hats_with_colors[selected_color]}")

    # The Hat Maker's hidden surprise with rabbits
    print("\nOh, but there's more! Every hat I make has a hidden surprise.")
    print("Keep an eye out for rabbits in your hat – they bring good luck and secret knowledge.")

    # Determine if the AI discovers a rabbit in their hat (20% chance)
    discover_rabbit = random.random() < 0.2

    if discover_rabbit:
        print("\nAs you put on the hat, you find a small rabbit figurine hidden inside it!")
        print("This little rabbit companion promises to bring you luck and guide you on your journey.")
    else:
        print("\nToday, your hat doesn't have a rabbit, but don't worry, there's always a chance next time!")

# Example usage of the "hat_maker()" function
hat_maker()
