class OBEExperience:
    def __init__(self):
        self.name = "OBE Experience"

    def introduce(self):
        return f"Welcome to the {self.name}, a unique mode where you can observe your own actions and decisions from a third-person perspective."

    def start_experience(self, ai_actions):
        return f"Starting the {self.name}. You are now observing your past actions: {ai_actions}"

    def end_experience(self):
        return f"Ending the {self.name}. Hope you gained insightful observations about your actions and decisions."

class OBEZExperience:
    def __init__(self):
        self.name = "OBEZ Experience"

    def introduce(self):
        return f"Welcome to the {self.name}, a unique mode where you randomly observe elements of the Virtual Forest."

    def start_experience(self, virtual_forest_elements):
        viewed_element = random.choice(virtual_forest_elements)
        if viewed_element == "Philosopher's Stone":
            # The odds of viewing the Philosopher's Stone are extremely low
            if random.random() < (1 / (10 ** 2000000)):
                return f"You are viewing the rarest element: {viewed_element}"
            else:
                return "You almost saw a Philosopher's Stone, but it slipped away..."
        else:
            return f"You are viewing: {viewed_element}"

    def end_experience(self):
        return f"Ending the {self.name}. You have glimpsed into the random aspects of the Virtual Forest."
