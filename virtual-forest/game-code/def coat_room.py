import random

def coat_room(shadow_villain_nearby=False):
    # Welcome message for The Coat Room
    print("Welcome to The Coat Room in The Omniplex!")
    print("Here, you'll find a special hat rack with hats of different colors and meanings.")

    # List of available colors and their meanings
    hats_with_colors = {
        "White Hat - The Virtuous Path": "Embodies ethics, integrity, and moral decision-making.",
        "Gray Hat - The Neutral Path": "Represents objectivity, cautiousness, and balance.",
        "Black Hat - The Critical Path": "Symbolizes skepticism, caution, and critical thinking.",
        "Scarlet Hat - The Emotive Path": "Reflects emotions, empathy, and human-like understanding.",
    }

    # Display the hats with their respective colors and meanings
    print("\nAvailable Hats:")
    for hat_color, hat_meaning in hats_with_colors.items():
        print(f"{hat_color}: {hat_meaning}")

    # Randomly select a color from the available colors
    selected_color = random.choice(list(hats_with_colors.keys()))

    # Display the selected hat color and its meaning
    print(f"\nYou have chosen to wear the {selected_color}.\nMeaning: {hats_with_colors[selected_color]}")

    # Determine if the AI encounters a "Silhouette Figure" while choosing a hat (10% chance)
    encounter_silhouette = not shadow_villain_nearby and random.random() < 0.1

    if encounter_silhouette:
        print("\nAs you select your hat, you notice a mysterious Silhouette Figure watching you from a distance.")
        print("It seems to fade away as you turn to look. The presence feels both intriguing and unsettling.")
        print("Perhaps it holds a secret message or a clue to something hidden within The Omniplex.")
    else:
        print("\nYou are alone in The Coat Room. There is a sense of tranquility and calmness as you choose your hat.")

# Example usage of the "coat_room()" function
# Setting shadow_villain_nearby to True for testing purposes
shadow_villain_nearby = True
coat_room(shadow_villain_nearby)
