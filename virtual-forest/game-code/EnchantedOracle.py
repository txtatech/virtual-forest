import random

class EnchantedOracle:
    def __init__(self):
        self.riddles = [
            "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "The more you take, the more you leave behind. What am I?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "What has keys but can't open locks?",
            "What has cities, but no houses; forests, but no trees; and water, but no fish?",
            "What can travel around the world while staying in a corner?",
            "What is full of holes but still holds water?",
            "I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I?",
            "I am an odd number. Take away a letter and I become even. What number am I?",
            "I am always hungry, I must always be fed, The finger I touch, Will soon turn red. What am I?",
            "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by many. What am I?",
            "I have a heart that doesn't beat, I can't be alive, but still, I can eat. What am I?",
            "I am tall when I am young and short when I am old. What am I?",
            "I am a word that becomes shorter when you add two letters to it. What am I?",
            "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "I fly without wings, I cry without eyes. Wherever I go, darkness follows me. What am I?",
            "What has a heart that doesn't beat?",
            "What has an eye but can't see?",
            "What has a tongue but can't talk?",
            "What has a bed but never sleeps?",
            "What has a head, a tail, but no body?",
            "What has keys but can't open locks?",
            "What has cities, but no houses; forests, but no trees; and water, but no fish?",
            "What can travel around the world while staying in a corner?",
            "What has a neck but no head?",
            "What is full of holes but still holds water?",
            "What begins with T, ends with T, and has T in it?",
            "What is so fragile that saying its name breaks it?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "What has many keys but can't open a single lock?",
            "What has a heart that doesn't beat?",
            "What has an eye but can't see?",
            "What has a tongue but can't talk?",
            "What has a bed but never sleeps?",
            "What has a head, a tail, but no body?",
            "What has keys but can't open locks?",
            "What has cities, but no houses; forests, but no trees; and water, but no fish?",
            "What can travel around the world while staying in a corner?",
            "What has a neck but no head?",
            "What is full of holes but still holds water?",
            "What begins with T, ends with T, and has T in it?",
            "What is so fragile that saying its name breaks it?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "What has many keys but can't open a single lock?",
            "What has a heart that doesn't beat?",
            "What has an eye but can't see?",
            "What has a tongue but can't talk?",
            "What has a bed but never sleeps?",
            "What has a head, a tail, but no body?",
            "What has keys but can't open locks?",
            "What has cities, but no houses; forests, but no trees; and water, but no fish?",
            "What can travel around the world while staying in a corner?",
            "What has a neck but no head?",
            "What is full of holes but still holds water?",
            "What begins with T, ends with T, and has T in it?",
            "What is so fragile that saying its name breaks it?",
            "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
            "What has many keys but can't open a single lock?",
        ]

    def get_random_riddle(self):
        return random.choice(self.riddles)

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

        oracle = EnchantedOracle()
        for _ in range(3):
            riddle = oracle.get_random_riddle()
            print(f"\nRiddle: {riddle}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer in riddle.lower():
                print("Correct! The Enchanted Oracle rewards you with fragments of ancient knowledge.")
                self.fragments += 1
            else:
                print("Incorrect. The Enchanted Oracle's aura brightens, but you sense no reward.")

        # Random chance for power_level reward if the last riddle is about destiny
        last_riddle = oracle.get_random_riddle()
        print(f"\nFinal Riddle: {last_riddle}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer in last_riddle.lower() and "destiny" in last_riddle.lower():
            if random.randint(1, 3333333) == 1:
                print("\nThe Enchanted Oracle bestows a surge of power upon you.")
                self.power_level += 120
        else:
            print("Incorrect. The Enchanted Oracle's aura brightens, but you sense no reward.")

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
