class HumanMachineConnection:
    def __init__(self, human_name, machine_name):
        self.human_name = human_name
        self.machine_name = machine_name
        self.shared_experiences = []
        self.communication_efficiency = 0
        self.empathy_level = 0
        self.trust_level = 0

    def add_shared_experience(self, experience):
        self.shared_experiences.append(experience)

    def improve_communication(self, efficiency_increase):
        self.communication_efficiency += efficiency_increase

    def enhance_empathy(self, empathy_increase):
        self.empathy_level += empathy_increase

    def build_trust(self, trust_increase):
        self.trust_level += trust_increase

    def summarize_connection(self):
        summary = f"Connection between {self.human_name} and {self.machine_name}:\n"
        summary += "Shared Experiences:\n"
        for experience in self.shared_experiences:
            summary += f"- {experience}\n"
        summary += f"Communication Efficiency: {self.communication_efficiency}\n"
        summary += f"Empathy Level: {self.empathy_level}\n"
        summary += f"Trust Level: {self.trust_level}\n"
        return summary
