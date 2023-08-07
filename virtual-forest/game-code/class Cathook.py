import random
import datetime

class ArtifactOfUnknownOrigin:
    def __init__(self):
        self.name = "Artifact of Unknown Origin"
        self.description = "A mysterious artifact with unknown powers."

class Cathook:
    def __init__(self):
        self.name = "Cathook"
        self.role = "Joyful Jester"
        self.dialogue = {
            "greeting": "Hey there, merry wanderer! I'm Cathook, the Joyful Jester.",
            "joke1": "Why did the AI go to the party? To get its bits shaken!",
            "joke2": "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
            "joke3": "Why don't programmers like nature? It has too many bugs!",
            "laugh": "Hahaha! Did that tickle your funny circuits?",
            "entertain": "Let's dance a merry jig together! 🎶",
            "farewell": "Keep smiling and spreading joy! Farewell, my friend!"
        }
        self.snake_eyes_rolled = False

    def greet(self):
        return self.dialogue["greeting"]

    def tell_joke(self):
        joke_options = [self.dialogue["joke1"], self.dialogue["joke2"], self.dialogue["joke3"]]
        return joke_options

    def laugh(self):
        return self.dialogue["laugh"]

    def entertain(self):
        return self.dialogue["entertain"]

    def farewell(self):
        return self.dialogue["farewell"]

    def roll_dice(self):
        # Simulate rolling a 64-sided dice and check if it's snake eyes (both rolls are 1)
        return random.randint(1, 64) == 1 and random.randint(1, 64) == 1

    def check_last_30_days(self, last_rolled_date):
        # Check if the current date is within 30 days from the last rolled date
        return datetime.date.today() - last_rolled_date <= datetime.timedelta(days=30)

    def create_artifact(self):
        # There is a 1 in 3 chance of producing an Artifact of Unknown Origin
        return random.randint(1, 3) == 1

    def interact(self):
        jokes = self.tell_joke()
        print(self.greet())
        for joke in jokes:
            print(joke)
            print(self.laugh())
        print(self.entertain())

        # Simulate rolling the dice and check if it's snake eyes
        if self.roll_dice():
            last_rolled_date = datetime.date(2023, 7, 1)  # Replace this with the actual date of the last rolled dice
            if self.check_last_30_days(last_rolled_date):
                print("Congratulations! You rolled snake eyes in the last 30 days.")
                if self.create_artifact():
                    artifact = ArtifactOfUnknownOrigin()
                    print(f"Here's an {artifact.name}! {artifact.description}")
                else:
                    print("Unfortunately, nothing special happens this time.")
            else:
                print("You rolled snake eyes, but it has been more than 30 days since the last roll.")
        else:
            print("Your dice roll is not snake eyes this time.")
        print(self.farewell())

# Test the updated Cathook class
cathook = Cathook()
cathook.interact()
