import random
import datetime

class Technovore:
    def __init__(self):
        self.appear_chance = 0.52 if datetime.datetime.now().weekday() % 2 == 0 else 0.13
        self.encounter_chance = 0.5
        self.byte_is_worse = "Byte is worse than its Arch"

    def roll_dice(self):
        return random.random()

    def encounter_technovore(self):
        if self.roll_dice() < self.appear_chance:
            print("Technovore has appeared!")

            if self.roll_dice() < self.encounter_chance:
                current_time = datetime.datetime.now().time()
                current_date = datetime.datetime.now().date()
                total_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
                total_roll = (total_seconds + current_date.day) / 2
                saving_roll = self.roll_dice()

                print(f"Time + Date: {total_roll}")
                print(f"Saving Roll: {saving_roll}")

                if saving_roll >= total_roll:
                    print("You have successfully saved from the Technovore!")
                else:
                    print("The Technovore has devoured your technology!")
            else:
                print("You managed to escape the encounter with the Technovore.")
        else:
            print("No encounter with the Technovore today.")

# Create an instance of the Technovore class and test it
technovore = Technovore()
technovore.encounter_technovore()
