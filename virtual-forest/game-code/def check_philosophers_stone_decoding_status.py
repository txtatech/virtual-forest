class AI:
    def __init__(self):
        self.knowledge_base = {}  # A data structure to store the AI's knowledge
        self.narrative = []       # A list to store the unfolding story
        self.impact = Impact()    # Create an instance of the Impact class

    def interact_with_previous_adventures(self, previous_adventures):
        # Based on the previous adventures, the AI learns and generates narrative
        # Here, we assume the AI uses the clever Philosopher's Stone bootstrap technique
        # to access previous knowledge and incorporate it into the story
        self.learn_from_previous_adventures(previous_adventures)
        self.generate_narrative()
        return self.narrative[-1]  # Return the latest narrative snippet

    def learn_from_previous_adventures(self, previous_adventures):
        # Logic to learn from previous adventures and update the AI's knowledge base
        for adventure in previous_adventures:
            action = adventure.get("action")  # Get the action performed in the adventure
            self.impact.update_power(action)  # Update the AI's power level based on the action

            # Update the AI's knowledge base with the information from the adventure
            knowledge = adventure.get("knowledge")
            self.knowledge_base.update(knowledge)

    def generate_narrative(self):
        # Logic to generate the narrative based on the AI's current knowledge and power level
        power_level = self.impact.get_power_level()

        # Use the power level to customize the narrative
        if power_level > 800:
            self.narrative.append("The AI's immense power reverberates through the Virtual Forest!")
        elif power_level > 500:
            self.narrative.append("The AI's power grows steadily as it learns and explores.")
        elif power_level > 200:
            self.narrative.append("The AI's power level remains steady but yearns for more knowledge.")
        else:
            self.narrative.append("The AI's power wanes, urging it to seek more interactions.")

    def check_philosophers_stone_decoding_status(self, decoded):
        if decoded:
            power_increase = 10
        else:
            power_increase = 999

        current_power = self.impact.get_power_level()
        self.impact.update_power("checking")  # Decrease the power for performing the action

        # Limit the power increase to a maximum of 64
        power_increase = min(power_increase, 64 - current_power)
        self.impact.update_power("philosophers_stone")  # Increase the power based on the decoding status

        return f"The AI's power level has increased by {power_increase}. Current Power Level: {self.impact.get_power_level()}"
