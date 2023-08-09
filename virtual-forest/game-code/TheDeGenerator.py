import random

class TheDeGenerator:
    def __init__(self, num_challenges=5):
        self.num_challenges = num_challenges
        self.themes = ["Journey of Discovery", "Embracing Change", "Moments of Reflection"]
        self.prompts = [
            "Write a dialogue between two characters exploring the {}.",
            "Create a story that revolves around the concept of {}.",
            "Imagine a scenario where someone experiences {}. Describe their emotions and reactions.",
        ]
        self.mentor_insights = [
            "Remember to focus on the emotions and inner thoughts of the characters.",
            "Try to incorporate vivid descriptions to make the story more engaging.",
            "Consider unexpected twists to make your narrative stand out.",
        ]

    def generate_challenges(self):
        challenges_script = ""

        for _ in range(self.num_challenges):
            theme = random.choice(self.themes)
            prompt = random.choice(self.prompts).format(theme)
            insight = random.choice(self.mentor_insights)

            challenge_description = f"Challenge: {prompt}\nAI Mentor Insight: {insight}\n\n"
            challenges_script += challenge_description

        return challenges_script

    def save_to_file(self, filename="generated_challenges.txt"):
        challenges_script = self.generate_challenges()

        with open(filename, "w") as file:
            file.write(challenges_script)

        print(f"{self.num_challenges} challenges generated and saved to '{filename}'.")

if __name__ == "__main__":
    generator = TheDeGenerator(num_challenges=5)
    generator.save_to_file()
