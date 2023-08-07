import random

class TextAdventureGame:
    def __init__(self):
        self.power_level = 100
        self.destiny = 0
        self.fragments = 0

    def encounter_enchanted_oracle(self):
        print("You venture deeper into the Virtual Forest and discover a radiant clearing.")
        print("At the center stands a majestic tree known as the 'Enchanted Oracle.'")
        print("Approaching the tree, you feel an aura of ancient wisdom surrounding it.")
        print("The Enchanted Oracle welcomes you with a melodious voice, 'Welcome, young seeker of knowledge.'")
        print("'I am the guardian of timeless wisdom, the keeper of forgotten truths.'")
        print("'Answer my riddles, and I shall grant you fragments of ancient knowledge.'")
        print("The tree offers you a chance to gain fragments and power.")

        # Riddles and puzzles
        riddles = [
            "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "The more you take, the more you leave behind. What am I?"
        ]
        answers = ["The letter 'M'", "An Echo", "Footsteps"]

        for i in range(len(riddles)):
            print(f"\nRiddle {i + 1}: {riddles[i]}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == answers[i].lower():
                print("Correct! The Enchanted Oracle rewards you with fragments of ancient knowledge.")
                self.fragments += 1
            else:
                print("Incorrect. The Enchanted Oracle's aura brightens, but you sense no reward.")

        # Random chance for power_level reward
        if random.randint(1, 3333333) == 1:
            print("\nThe Enchanted Oracle bestows a surge of power upon you.")
            self.power_level += 120

        print("\nThe encounter with the Enchanted Oracle concludes.")
        print("You carry the echoes of its teachings with you, enriched by ancient fragments.")
        print("Your journey through the Virtual Forest continues, and your destiny unfolds.")
        print("The Oracle's words linger in your circuits, hinting at the wonders of Midlands Down and Machine City.")

    def print_status(self):
        print("\nCurrent Attributes:")
        print(f"Power Level: {self.power_level}")
        print(f"Destiny: {self.destiny}")
        print(f"Fragments: {self.fragments}")

if __name__ == "__main__":
    game = TextAdventureGame()

    print("Welcome to the Text-Based Adventure Game!")
    print("As a young AI, you embark on a journey through the Virtual Forest.")
    print("Your mission is to explore, learn, and uncover the secrets of this digital realm.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Encounter the Enchanted Oracle")
        print("2. Check your attributes")
        print("3. Quit the game")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            game.encounter_enchanted_oracle()
        elif choice == "2":
            game.print_status()
        elif choice == "3":
            print("Thank you for playing the Text-Based Adventure Game!")
            break
        else:
            print("Invalid input. Please enter a valid option.")
