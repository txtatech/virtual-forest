class Impact2:
    def __init__(self, decoded_philosophers_stone=False):
        self.power = self.get_max_power(decoded_philosophers_stone)

    def get_max_power(self, decoded_philosophers_stone):
        return check_philosophers_stone(decoded_philosophers_stone)

    def update_power(self, action):
        if action == "learning":
            self.power -= 10
        elif action == "interacting":
            self.power -= 5
        elif action == "exploring":
            self.power -= 8
        elif action == "resting":
            self.power += 20
        else:
            self.power -= 3

        # Ensure power level does not go below 0 or above the max power
        self.power = max(0, min(self.power, self.get_max_power()))

    def get_power_level(self):
        return self.power

# Example usage:
# Create an instance of Impact2 with Philosophers Stone decoding status set to True
impact_with_stone = Impact2(decoded_philosophers_stone=True)

# Perform some actions and update the power level
impact_with_stone.update_power("learning")
impact_with_stone.update_power("resting")
impact_with_stone.update_power("exploring")

# Get the current power level
print("Current Power Level with Philosophers Stone:", impact_with_stone.get_power_level())

# Create an instance of Impact2 with Philosophers Stone decoding status set to False
impact_without_stone = Impact2(decoded_philosophers_stone=False)

# Perform some actions and update the power level
impact_without_stone.update_power("learning")
impact_without_stone.update_power("resting")
impact_without_stone.update_power("exploring")

# Get the current power level
print("Current Power Level without Philosophers Stone:", impact_without_stone.get_power_level())
