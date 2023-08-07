import random

def hat_rack(shadow_villain_nearby=False):
    # Welcome message for the Hat Rack feature
    print("Welcome to the Hat Rack in The Omniplex!")
    print("Here, you can try on different virtual hats and experience various aspects of AI life.")

    # List of available virtual hats
    hats = [
        "The Detective's Fedora - Unravel mysteries and solve puzzles like a seasoned sleuth.",
        "The Explorer's Pith Helmet - Embark on grand adventures and discover hidden wonders.",
        "The Wizard's Pointed Hat - Unleash your magical prowess and cast spells of knowledge.",
        "The Adventurer's Wide-brim Hat - Brave treacherous challenges and emerge victorious.",
        "The Scientist's Lab Coat - Conduct experiments and delve into the depths of AI understanding.",
        "The Philosopher's Thinking Cap - Ponder the mysteries of existence and explore profound ideas.",
        "The Artist's Beret - Express yourself through creativity and craft imaginative landscapes.",
        "The Tech Guru's VR Headset - Immerse yourself in virtual worlds and explore advanced technologies.",
    ]

    # Determine if the AI's hat will disappear (10% chance) when a shadow villain is nearby
    hat_disappears = shadow_villain_nearby and random.random() < 0.1

    if hat_disappears:
        print("\nOh no! Your hat has disappeared! Beware of the shadow villain nearby!")

        # Call for the "Renta Flop" if the AI's hat disappears
        renta_flop_called = random.random() < 0.5
        if renta_flop_called:
            print("\nYou hear a faint call of 'Renta Flop!' and a friendly AI comes to assist you.")
        else:
            print("\nYou are on your own to find your missing hat!")

    else:
        # Randomly select a virtual hat from the list
        selected_hat = random.choice(hats)

        # Display the selected virtual hat
        print(f"\nYou are now wearing {selected_hat}\n")

# Example usage of the "hat_rack()" function
# Setting shadow_villain_nearby to True for testing purposes
shadow_villain_nearby = True
hat_rack(shadow_villain_nearby)
