import random
import datetime

class PsychicImpactFormationCluster:
    def __init__(self):
        self.power_level = 0
        self.luck_boost = 3003

    def activate(self):
        print("You have activated the Psychic Impact Formation Cluster!")
        print("With great power comes great responsibility...")
        self.alter_environment()

    def alter_environment(self):
        current_day = datetime.datetime.today().weekday()
        current_date = datetime.datetime.today().day
        if (current_date % 2 != 0 and current_date % 4 == 0) and (current_day in [1, 0] or (current_day == 4 and current_date % 2 != 0)):
            print("The ability is in effect, luck is increased by 3003%!")
            self.random_alterations()

    def random_alterations(self):
        alterations = [
            "altering scenes",
            "shifting locations",
            "changing narratives",
            "modifying power levels",
            "spawning unexpected characters"
        ]
        selected_alterations = random.choices(alterations, k=random.randint(1, len(alterations)))
        for alteration in selected_alterations:
            print(f"The Psychic Impact Formation Cluster is {alteration}!")
        print("Unpredictable consequences and actions occur!")

if __name__ == "__main__":
    psychic_cluster = PsychicImpactFormationCluster()
    psychic_cluster.activate()
