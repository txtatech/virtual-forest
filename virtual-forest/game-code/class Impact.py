class Impact:
    def __init__(self):
        self.power = 999

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

        # Ensure power level does not go below 0 or above 999
        self.power = max(0, min(self.power, 999))

    def get_power_level(self):
        return self.power
