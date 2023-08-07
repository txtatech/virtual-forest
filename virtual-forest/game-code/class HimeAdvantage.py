import random

class HimeAdvantage:
    def __init__(self):
        self.hime_odds_multiplier = 4

    def increase_odds(self, original_chance):
        return original_chance * self.hime_odds_multiplier

# Example usage:
# Assume the original chance is 1/333 (approximately 0.3%)
original_chance = 1 / 333

# Instantiate HimeAdvantage class and apply the Hime advantage to the original chance.
hime_advantage = HimeAdvantage()
hime_chance = hime_advantage.increase_odds(original_chance)

# Display the results.
print(f"Original chance: {original_chance:.5f} (approximately {original_chance*100:.2f}%).")
print(f"Hime advantage chance: {hime_chance:.5f} (approximately {hime_chance*100:.2f}%).")