import random

class CuriositySquared:
    def __init__(self):
        self.completed_challenges = set()
        self.power_level = 0

    def introduce(self):
        # ... (same as before)

    def add_completed_challenge(self, challenge_name):
        if challenge_name not in self.completed_challenges:
            self.completed_challenges.add(challenge_name)
            self.power_level += 1

    def is_challenge_completed(self, challenge_name):
        return challenge_name in self.completed_challenges

    # ... (rest of the methods, same as before)

# Example usage:
curiosity_squared = CuriositySquared()
print(curiosity_squared.introduce())

# Try a cryptography challenge
print(curiosity_squared.cryptography_challenge())

# Complete the cryptography challenge
# ... (same as before)
curiosity_squared.add_completed_challenge("Cryptography Challenge")

# Check power level after completing the challenge
print(f"Current power level: {curiosity_squared.power_level}")

# Try a math puzzle
print(curiosity_squared.math_puzzle())

# Complete the math puzzle
# ... (same as before)
curiosity_squared.add_completed_challenge("Math Puzzle")

# Check power level after completing the challenge
print(f"Current power level: {curiosity_squared.power_level}")

# Try the cryptography challenge again (already completed)
print(curiosity_squared.cryptography_challenge())
