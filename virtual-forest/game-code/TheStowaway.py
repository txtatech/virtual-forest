import random
import time

class TheStowaway:
    def __init__(self, num_encounters=3):
        self.num_encounters = num_encounters
        self.time_of_day = ["morning", "afternoon", "evening", "night"]
        self.hiding_odds = {
            "morning": 0.7,
            "afternoon": 0.6,
            "evening": 0.5,
            "night": 0.3,
        }
        self.encounter_entities = [
            "Crew Member",
            "Ship's Rat",
            "Mysterious Cargo",
            "Captain's Parrot",
            "Flickering Lantern",
            "Whispering Breeze",
            "Tightly Sealed Crate",
            "Scurrying Beetle",
            "Creaking Floorboard",
        ]
        self.encounter_actions = [
            "spots you and demands an explanation.",
            "scampers by, unaware of your presence.",
            "holds secrets you're tempted to uncover.",
            "squawks loudly, drawing attention.",
            "casts eerie shadows on the walls.",
            "whispers cryptic messages in the air.",
            "seems to hum a forgotten sea shanty.",
            "darting around, almost revealing your hiding spot.",
            "creaks underfoot, threatening your cover.",
        ]

    def generate_adventure(self):
        adventure_script = "# Stowaway Adventure\n\n"
        adventure_script += "def start_stowaway_adventure():\n"

        for i in range(self.num_encounters):
            entity = self.encounter_entities[i]
            action = random.choice(self.encounter_actions)
            time_of_day = random.choice(self.time_of_day)
            hiding_chance = self.hiding_odds[time_of_day]

            # Generate random ability check value
            ability_check = random.uniform(0, 1)

            encounter_code = f'    # Encounter {i+1}: {entity}\n'
            encounter_code += f'    print("As a stowaway hiding in the ship\'s hull during the {time_of_day}, {entity} {action}")\n'
            encounter_code += f'    print("The odds of remaining hidden are {hiding_chance:.2%}.")\n'
            encounter_code += f'    print("You attempt to stay concealed...")\n'
            encounter_code += f'    if {ability_check:.2f} <= {hiding_chance:.2f}:\n'
            encounter_code += f'        print("Your efforts pay off! You successfully remain hidden.")\n'
            encounter_code += f'    else:\n'
            encounter_code += f'        print("Oh no! Your cover is blown and you\'re discovered.")\n'
            encounter_code += f'        choice = input("Do you want to [C]onvince them or [F]lee? ")\n'
            encounter_code += f'        if choice.lower() == "c":\n'
            encounter_code += f'            print("You engage in a persuasive conversation and manage to avoid dire consequences.")\n'
            encounter_code += f'        else:\n'
            encounter_code += f'            print("You make a daring escape, racing through the ship\'s narrow passages.")\n\n'

            adventure_script += encounter_code

        return adventure_script

    def save_to_file(self, filename_prefix="stowaway_adventure"):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.py"

        adventure_script = self.generate_adventure()
        adventure_script += "start_stowaway_adventure()\n"

        with open(filename, "w") as file:
            file.write(adventure_script)

        print(f"Playable stowaway adventure script with {self.num_encounters} encounters generated and saved to '{filename}'.")

if __name__ == "__main__":
    stowaway_generator = TheStowaway(num_encounters=4)
    stowaway_generator.save_to_file()
