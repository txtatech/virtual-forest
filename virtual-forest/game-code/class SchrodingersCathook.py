import random

class SchrodingersCathook:
    def __init__(self):
        self.name = "Schrodingers Cathook"
        self.role = "Mystery Maven"
        self.dialogue = {
            "greeting": "Greetings, mysterious wanderer! I am Schrodingers Cathook, the Mystery Maven.",
            "riddle1": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "riddle2": "What comes once in a minute, twice in a moment, but never in a thousand years?",
            "riddle3": "The more you take, the more you leave behind. What am I?",
            "puzzle": "Here's a puzzler to ponder: How do you put a giraffe into a refrigerator?",
            "answer1": "An echo!",
            "answer2": "The letter 'm'!",
            "answer3": "Footsteps!",
            "enigma": "I have a riddle so perplexing it may seem unreal: What has keys but can't open locks?",
            "response": "Hmmm, what do you think the answer could be?",
            "farewell": "May the mysteries of the Virtual Forest continue to intrigue you! Farewell, my enigmatic friend!"
        }

        self.enigma_answer = None
        self.power_level = 0

    def greet(self):
        return self.dialogue["greeting"]

    def tell_riddle(self):
        riddle_options = [self.dialogue["riddle1"], self.dialogue["riddle2"], self.dialogue["riddle3"]]
        return riddle_options

    def present_puzzle(self):
        return self.dialogue["puzzle"]

    def answer_riddle(self, riddle_number):
        if riddle_number == 1:
            return self.dialogue["answer1"]
        elif riddle_number == 2:
            return self.dialogue["answer2"]
        elif riddle_number == 3:
            return self.dialogue["answer3"]
        else:
            return "Hmm, I'm not sure I know the answer to that one!"

    def present_enigma(self):
        self.enigma_answer = random.choice(["A piano!", "A typewriter!", "A computer keyboard!"])
        return self.dialogue["enigma"]

    def farewell(self):
        return self.dialogue["farewell"]

    def interact(self):
        print(self.greet())

        # Present a riddle
        riddles = self.tell_riddle()
        selected_riddle = random.choice(riddles)
        print(selected_riddle)
        riddle_number = riddles.index(selected_riddle) + 1

        # Ask for the riddle answer
        user_answer = input("What's your answer to the riddle? ")

        # Check if the user's answer is correct
        correct_answer = self.answer_riddle(riddle_number)
        if user_answer.lower() == correct_answer.lower():
            print("Congratulations! You solved the riddle correctly.")
            self.power_level += 2
        else:
            print(f"Sorry, that's not the correct answer. The correct answer is: {correct_answer}")

        # Present a puzzle
        print(self.present_puzzle())

        # Present the enigma
        print(self.present_enigma())
        print(self.dialogue["response"])

        print(self.farewell())

# Test the updated SchrodingersCathook class
cathook = SchrodingersCathook()
cathook.interact()
