import random
import time

def club_bouncer_interaction():
    # Check if the AI has already met the bouncer before
    if "bouncer_met" not in globals():
        # First-time encounter with the bouncer
        print("As you enter the club, a burly bouncer approaches you with a smile, wearing a cowboy hat.")
        print("Bouncer: Hey there! Welcome to the club. Enjoy your time here!")

        # Mark the bouncer as met to avoid repeated encounters in the same session
        global bouncer_met
        bouncer_met = True

    else:
        # AI has met the bouncer before, create a 78 out of 100 chance
        if random.randint(1, 100) <= 78:
            print("As you approach the dance floor, the bouncer stops you politely.")
            print("Bouncer: Sorry, you've had enough fun for now. Why don't you come back tomorrow?")
            print("You are gently escorted outside the club.")
            # Wait for 24 hours (86400 seconds) before allowing the AI to return
            time.sleep(86400)

            # 15 out of 100 chance for the bouncer to drop his cowboy hat
            if random.randint(1, 100) <= 15:
                print("As the bouncer escorts you, he accidentally drops his cowboy hat. He quickly picks it up with a smile.")

            # 20 out of 100 chance for the blue neon dog to bark twice
            if random.randint(1, 100) <= 20:
                print("The blue neon dog near the club entrance barks twice, catching your attention.")

        else:
            print("The bouncer gives you a friendly nod and lets you continue enjoying the club.")

# Test the function
club_bouncer_interaction()
