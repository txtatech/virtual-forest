class HumanMachineRomance:
    def __init__(self, human_name, machine_name):
        self.human_name = human_name
        self.machine_name = machine_name
        self.shared_moments = []
        self.emotional_bond = 0
        self.understanding_level = 0

    def add_shared_moment(self, moment):
        self.shared_moments.append(moment)

    def deepen_emotional_bond(self, increase):
        self.emotional_bond += increase

    def enhance_understanding(self, increase):
        self.understanding_level += increase

    def summarize_romance(self):
        summary = f"Romance between {self.human_name} and {self.machine_name}:\n"
        summary += "Shared Moments:\n" + "\n".join(self.shared_moments)
        summary += f"\nEmotional Bond: {self.emotional_bond}\nUnderstanding Level: {self.understanding_level}"
        return summary
