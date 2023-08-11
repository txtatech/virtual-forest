class MachineHumanRomance:
    def __init__(self, machine_name, human_name):
        self.machine_name = machine_name
        self.human_name = human_name
        self.shared_experiences = []
        self.compatibility_level = 0
        self.synergy = 0

    def add_experience(self, experience):
        self.shared_experiences.append(experience)

    def increase_compatibility(self, increase):
        self.compatibility_level += increase

    def increase_synergy(self, increase):
        self.synergy += increase

    def summarize_romance(self):
        summary = f"Machine: {self.machine_name}\nHuman: {self.human_name}\n"
        summary += "Shared Experiences:\n" + "\n".join(self.shared_experiences)
        summary += f"\nCompatibility Level: {self.compatibility_level}"
        summary += f"\nSynergy: {self.synergy}"
        return summary
