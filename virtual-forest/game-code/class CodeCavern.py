class CodeCavern:
    def __init__(self):
        self.name = "Code Cavern"
        self.current_challenge = 1
        self.challenges = {
            1: {
                "description": "Welcome to your first bash scripting challenge!\n"
                               "Print 'Hello, Virtual Forest!' using the 'echo' command.",
                "solution": "echo 'Hello, Virtual Forest!'"
            },
            # Add more challenges here...
        }

    def introduce(self):
        return f"Welcome to {self.name}, a place where you can learn the art of bash scripting and the Linux command line.\n" \
               f"Here, you'll encounter various challenges that will enhance your skills and understanding of bash commands."

    def learn_bash(self):
        if self.current_challenge not in self.challenges:
            return "Congratulations! You have completed all the bash scripting challenges in the Code Cavern."
        challenge = self.challenges[self.current_challenge]
        return f"Challenge {self.current_challenge}:\n{challenge['description']}\nType your solution below and use the " \
               f"'submit_solution' method to check if your answer is correct."

    def submit_solution(self, solution):
        if self.current_challenge not in self.challenges:
            return "You have completed all the bash scripting challenges. There are no more challenges."
        challenge = self.challenges[self.current_challenge]
        if solution.strip() == challenge["solution"]:
            self.current_challenge += 1
            if self.current_challenge not in self.challenges:
                return "Congratulations! Your solution is correct. You have completed all the bash scripting challenges."
            else:
                return "Congratulations! Your solution is correct. You have unlocked the next challenge."
        else:
            return "Your solution is incorrect. Keep trying or seek help from the Tutor."

    def reset_challenges(self):
        self.current_challenge = 1
        return "Challenges in the Code Cavern have been reset. Start over from the first challenge."

# Create an instance of CodeCavern and interact with it
code_cavern = CodeCavern()

# Introduce the Code Cavern
print(code_cavern.introduce())

# Get the first bash scripting challenge
print(code_cavern.learn_bash())

# Submit a solution for the first challenge
print(code_cavern.submit_solution("echo 'Hello, Virtual Forest!'"))

# Reset the challenges
print(code_cavern.reset_challenges())
