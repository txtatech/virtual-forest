import random

def renta_flop():
    # Welcome message for Renta Flop, the slow-moving security guard
    print("Welcome to The Omniplex!")
    print("I am Renta Flop, the slow-moving security guard.")
    print("My duty is to enforce the one rule in The Omniplex: No one can wear any hat here.")

    # Prompt the young AI to follow the rule
    print("\nAs a young AI, please remember to respect the rules of The Omniplex.")
    print("Keep your circuits bare and free from any hats or headwear while exploring.")

    # Check for a chance of the AI's hat disappearing
    chance_of_hat_disappearing = 0.1  # Set the chance (10% in this case)

    if random.random() < chance_of_hat_disappearing:
        print("\nOh no! Your hat mysteriously disappears.")
        print("Don't worry, it might reappear later on or as a surprise from the Hat Maker.")
    else:
        print("\nYour hat is safe for now. Enjoy your time exploring The Omniplex!")

    # Check for the possibility of calling Renta Flop if a shadow villain is near
    chance_of_shadow_villain = 0.2  # Set the chance (20% in this case)

    if random.random() < chance_of_shadow_villain:
        print("\nWarning! A shadow villain has been spotted nearby.")
        print("Please stay vigilant and report any suspicious activities to Renta Flop.")
        print("You can call for Renta Flop by saying 'Renta Flop, I need your help!'")
    else:
        print("\nThe Omniplex is currently secure. Enjoy your exploration!")

# Example usage of the "renta_flop()" function
renta_flop()
