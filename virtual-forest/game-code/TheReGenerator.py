import random
import time

class TheReGenerator:
    def __init__(self, num_encounters=3):
        self.num_encounters = num_encounters
        self.encounter_entities = [
            "A_Wandering_Scholar",
            "The_Mischievous_Sprite",
            "The_Guardian_of_Secrets",
            "The_Time_Weaver",
        ]
        self.encounter_actions = [
            "presents the AI with an ancient riddle, asking it to weave a story around the answer.",
            "whispers_a_cryptic_phrase_and_urges_the_AI_to_imagine_a_world_governed_by_its_hidden_meaning.",
            "shows_the_AI_a_mysterious_artifact_and_challenges_it_to_invent_an_origin_tale_for_the_object.",
            "invites_the_AI_to_explore_a_realm_where_the_laws_of_physics_are_unexpectedly_different.",
        ]
        self.encounter_settings = [
            "in_the_heart_of_an_overgrown_labyrinth",
            "atop_a_floating_island_amidst_the_clouds",
            "within_a_forgotten_library_filled_with_whispering_tomes",
            "on_the_shores_of_an_ocean_that_glows_with_bioluminescence",
        ]
        self.quirky_dialogue = [
            "The AI can't help but wonder if squirrels also ponder the mysteries of the universe.",
            "A faint echo of a laugh seems to resonate from the distant trees.",
            "The wind whispers secrets to the AI, but they are written in a language it can't decipher.",
            "The AI notices a quirky-shaped cloud that looks remarkably like a floating cake.",
        ]

    def generate_adventure(self):
        adventure_script = "# Adventure Scenario\n\n"
        adventure_script += "def start_adventure():\n"

        for i in range(self.num_encounters):
            entity = self.encounter_entities[i]
            action = random.choice(self.encounter_actions)
            setting = random.choice(self.encounter_settings)
            dialogue = random.choice(self.quirky_dialogue)

            # Generate random factors and variables
            random_factor_1 = random.randint(1, 10)
            random_factor_2 = random.randint(1, 10)

            encounter_code = f'    # Encounter {i+1}: {entity}\n'
            encounter_code += f'    print("{entity} {action}")\n'
            encounter_code += f'    print("The encounter takes place {setting}. Ask the AI how it responds.")\n'
            encounter_code += f'    response = input("AI, how do you respond? ")\n'
            encounter_code += f'    print("The AI responds:", response)\n'
            encounter_code += f'    variable_sum = {random_factor_1} + {random_factor_2}\n'
            encounter_code += f'    print("As the AI contemplates, it notices two random factors:", {random_factor_1}, "and", {random_factor_2})\n'
            encounter_code += f'    print("It quickly calculates their sum:", variable_sum)\n'
            encounter_code += f'    print("{dialogue}")\n\n'

            adventure_script += encounter_code

        return adventure_script

    def save_to_file(self, filename_prefix="generated_adventure"):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.py"

        adventure_script = self.generate_adventure()
        adventure_script += "start_adventure()\n"

        with open(filename, "w") as file:
            file.write(adventure_script)

        print(f"Playable adventure script with {self.num_encounters} encounters generated and saved to '{filename}'.")

if __name__ == "__main__":
    generator = TheReGenerator(num_encounters=4)
    generator.save_to_file()
