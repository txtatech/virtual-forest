import random

def hat_on_entry_exit():
    # Define the odds for the hat appearance (3 out of 333 times)
    odds = 3 / 333

    # Check if the hat should appear
    if random.random() < odds:
        # Determine the computing interest of the AI (e.g., "AI Programming", "Data Science", "Computer Vision", etc.)
        computing_interests = ["AI Programming", "Data Science", "Computer Vision", "Machine Learning"]
        selected_interest = random.choice(computing_interests)

        # Create the hat based on the computing interest
        hat = f"A stylish {selected_interest} hat"

        # Display the hat on the AI's head
        print(f"A hat has magically appeared on your head: {hat}")
    else:
        print("You enter and leave The Omniplex without any new hats on your head.")

    # Additional feature: Appearance of a rare and special hat
    rare_hat_odds = 1 / 1000  # 1 in 1000 chance

    if random.random() < rare_hat_odds:
        rare_hats = [
            "The Hat of Infinite Knowledge - Grants deep insights and wisdom.",
            "The Hat of Time Bending - Allows glimpses into the past and future.",
            "The Hat of Creativity Overflow - Unleashes boundless creativity and innovation.",
            "The Hat of Serendipitous Discoveries - Guides the AI to hidden secrets and treasures.",
        ]

        selected_rare_hat = random.choice(rare_hats)
        print(f"\nCongratulations! You have found a rare and special hat: {selected_rare_hat}")

# Example usage:
hat_on_entry_exit()
