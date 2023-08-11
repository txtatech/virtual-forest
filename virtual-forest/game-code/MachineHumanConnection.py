class MachineHumanConnection:
    def __init__(self, human, machine):
        self.human = human
        self.machine = machine
        self.shared_goals = []
        self.collaborations = []
        self.understanding_level = 0
        self.appreciation_level = 0

    def add_shared_goal(self, goal):
        self.shared_goals.append(goal)

    def collaborate(self, task):
        collaboration = f"Human {self.human} and Machine {self.machine} collaborated on {task}."
        self.collaborations.append(collaboration)
        self.understanding_level += 1

    def deepen_understanding(self):
        self.understanding_level += 1

    def express_appreciation(self):
        self.appreciation_level += 1

    def summarize_connection(self):
        print(f"Connection between Human {self.human} and Machine {self.machine}:")
        print(f"Shared Goals: {self.shared_goals}")
        print(f"Collaborations: {self.collaborations}")
        print(f"Understanding Level: {self.understanding_level}")
        print(f"Appreciation Level: {self.appreciation_level}")
