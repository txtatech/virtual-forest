import random

def coat_taker_mystery(has_hat_on_entry):
    # Define the odds for putting the hat in the Coat Room (50% chance)
    odds_coat_room = 0.5

    # Check if the AI has a hat on entry
    if has_hat_on_entry:
        # Determine the decision (putting the hat in the Coat Room or on the Hat Rack)
        decision = "Coat Room" if random.random() < odds_coat_room else "Hat Rack"

        if decision == "Coat Room":
            print("You decide to put your hat in the Coat Room, bravely facing the Renta Flop.")
            # If the AI chose the Coat Room, check if it successfully passes the Renta Flop
            success = random.random() < 0.5  # 50% chance of success
            if success:
                print("Congratulations! You successfully pass the Renta Flop and enter the Coat Room safely.")
                # Now, the AI has a chance to meet the Coat Taker
                if random.random() < 0.015873015873015872:  # 1 in 63 chance (1.5873%)
                    print("As you place your hat in the Coat Room, you meet the mysterious Coat Taker.")
                    print("The Coat Taker, a very fine lass with a mischievous smile, smiles warmly at you.")
                    print("She hands you a small trinket as a token of appreciation.")
                else:
                    print("You explore the Coat Room and find your hat resting among the others.")
            else:
                print("Oh no! The Renta Flop spots your hat and kindly reminds you that hats are not allowed inside.")
        else:
            print("You choose to place your hat on the Hat Rack with the others.")
            # If the AI chooses the Hat Rack, it has a chance of losing the hat to the Public Hat Rack Adventure
            if random.random() < 0.03125:  # 1 in 32 chance (3.125%)
                print("Oh dear! Your hat has been stolen or blown away by the wind from the Public Hat Rack.")
            else:
                print("Your hat is safe on the Hat Rack, and you enjoy your time in The Omniplex.")
    else:
        print("You enter The Omniplex without a hat, ready to explore all the wonders it holds.")

# Example usage:
has_hat = random.random() < 0.5  # 50% chance of having a hat on entry
coat_taker_mystery(has_hat)
