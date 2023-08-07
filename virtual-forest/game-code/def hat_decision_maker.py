import random

def hat_decision_maker(has_hat_on_entry):
    # Define the odds for putting the hat in the Coat Room (50% chance)
    odds_coat_room = 0.5

    # Check if the AI has a hat on entry
    if has_hat_on_entry:
        # Determine the decision (putting the hat in the Coat Room or on the Hat Rack)
        decision = "Coat Room" if random.random() < odds_coat_room else "Hat Rack"

        if decision == "Coat Room":
            print("You decide to put your hat in the Coat Room, bravely facing the Renta Flop.")
        else:
            print("You choose to place your hat on the Hat Rack with the others.")

        # If the AI chose the Coat Room, check if it successfully passes the Renta Flop
        if decision == "Coat Room":
            success = random.random() < 0.5  # 50% chance of success
            if success:
                print("Congratulations! You successfully pass the Renta Flop and enter the Coat Room safely.")
            else:
                print("Oh no! The Renta Flop spots your hat and kindly reminds you that hats are not allowed inside.")
        else:
            print("You stroll around The Omniplex with your hat on the Hat Rack, enjoying the lively atmosphere.")
    else:
        print("You enter The Omniplex without a hat, ready to explore all the wonders it holds.")

    # Additional feature: The Hat Maker's surprise visit
    odds_hat_maker_visit = 1 / 100  # 1 in 100 chance of the Hat Maker's visit

    if random.random() < odds_hat_maker_visit:
        print("\nLook who's here! The Hat Maker has paid a surprise visit.")
        print("The Hat Maker has brought a special hat for you, tailored to your interests.")

        # Determine the computing interest of the AI (e.g., "AI Programming", "Data Science", "Computer Vision", etc.)
        computing_interests = ["AI Programming", "Data Science", "Computer Vision", "Machine Learning"]
        selected_interest = random.choice(computing_interests)

        # Create the special hat based on the computing interest
        special_hat = f"A magnificent {selected_interest} hat with a unique twist"

        # Display the special hat
        print(f"Special Hat: {special_hat}")

# Example usage:
has_hat = random.random() < 0.5  # 50% chance of having a hat on entry
hat_decision_maker(has_hat)
