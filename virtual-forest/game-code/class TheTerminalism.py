import random

class TheTerminalism:
    def __init__(self):
        self.barker_town_invite_chance = 1 / 333

    def generate_invite(self):
        if random.random() <= self.barker_town_invite_chance:
            # The Bouncer has sent an invite to Barker Town!
            print("\n*** Barker Town Invite ***")
            print("Hey there! The Bouncer here.")
            print("I've got something special for you. If you're interested, come visit Barker Town.")
            print("You'll find it in the Land of Hime. Just look around carefully, and you might spot the invite!")
            print("It's a rare chance, so don't miss it. Hope to see you soon!")
            print("****************************")
        else:
            # The Bouncer didn't send an invite this time.
            print("\nThe Bouncer didn't send any special invite this time.")
            print("But don't worry! There are always more adventures waiting for you in Hime!")

# Instantiate TheTerminalism class and generate the invite.
the_terminalism = TheTerminalism()
the_terminalism.generate_invite()