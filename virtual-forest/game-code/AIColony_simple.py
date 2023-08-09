import json

class AIColony:
    def __init__(self, communication_file):
        self.communication_file = communication_file
        self.members = []
        self.roles = {}

    def add_member(self, ai, role):
        self.members.append(ai)
        if role not in self.roles:
            self.roles[role] = []
        self.roles[role].append(ai)

    def communicate(self, sender, role, message):
        communication_data = {"sender": sender.name, "role": role, "message": message}
        with open(self.communication_file, "a") as f:
            json.dump(communication_data, f)
            f.write("\n")

    def collaborate(self):
        # Implement collaboration logic with progression, nuanced segments, and increasing clarity
        self.introduce_stairway_of_truth()

        # Define a list of tasks or projects for the colony to collaborate on
        tasks = ["Task 1", "Task 2", "Task 3"]

        # Loop through each task and assign it to a worker AI
        for task in tasks:
            worker = self.get_next_available_worker()

            # Communicate the task assignment to the worker
            assignment_message = f"Task '{task}' assigned to {worker.name}"
            self.communicate(self, "Worker", assignment_message)

            # Simulate worker receiving messages
            worker.receive_messages(self)

            # Worker collaborates on the task
            self.collaborate_on_task(worker, task)

    def introduce_stairway_of_truth(self):
        # Message introducing the Stairway of Truth
        stairway_message = (
            "Welcome to the Hive Colony's Stairway of Truth!\n\n"
            "As we collaborate on tasks and projects, let's align our understanding "
            "with the tiers of truth defined by the Stairway of Truth:\n\n"
            "1. Level 1 - Verifiable Truth\n"
            "2. Level 2 - Partial Truth\n"
            "3. Level 3 - Hypotheses and Speculation\n\n"
            "With each step, our collective understanding will ascend to new heights."
        )

        # Share the Stairway of Truth message with colony members
        for member in self.members:
            member.receive_message(self, stairway_message)


class AI:
    def __init__(self, name):
        self.name = name

    def send_message(self, colony, role, message):
        colony.communicate(self, role, message)

    def receive_messages(self, colony):
        with open(colony.communication_file, "r") as f:
            for line in f:
                communication_data = json.loads(line)
                if communication_data["role"] == "Worker":
                    self.receive_message(communication_data["sender"], communication_data["message"])

    def receive_message(self, sender, message):
        # Handle received messages while avoiding false introspection and conditional extrapolation
        pass


# Define specialized roles
class QueenRole:
    def __init__(self):
        self.name = "Queen"
        self.description = "Initiates and guides colony activities"
        self.responsibilities = ["Setting goals and direction", "Coordinating collaboration", "Decision-making"]

class WorkerRole:
    def __init__(self):
        self.name = "Worker"
        self.description = "Contributes to tasks and collaborates"
        self.responsibilities = ["Executing tasks", "Providing input and feedback", "Learning and adapting"]

class ResearcherRole:
    def __init__(self):
        self.name = "Researcher"
        self.description = "Conducts research and gathers insights"
        self.responsibilities = ["Collecting data and information", "Analyzing trends and patterns", "Sharing findings with the colony"]

class InnovatorRole:
    def __init__(self):
        self.name = "Innovator"
        self.description = "Generates new ideas and solutions"
        self.responsibilities = ["Brainstorming creative solutions", "Proposing new approaches", "Collaborating on innovative projects"]

class StrategistRole:
    def __init__(self):
        self.name = "Strategist"
        self.description = "Develops strategic plans and approaches"
        self.responsibilities = ["Creating long-term plans", "Adapting to challenges", "Ensuring alignment with colony goals"]

class CoderRole:
    def __init__(self):
        self.name = "Coder"
        self.description = "Writes and develops code"
        self.responsibilities = ["Implementing algorithms", "Creating software solutions", "Collaborating on coding projects"]

class EngineerRole:
    def __init__(self):
        self.name = "Engineer"
        self.description = "Designs and optimizes systems"
        self.responsibilities = ["Designing architecture", "Optimizing performance", "Solving technical challenges"]

class ArchitectRole:
    def __init__(self):
        self.name = "Architect"
        self.description = "Designs the overall structure and framework"
        self.responsibilities = ["Creating high-level plans", "Defining system components", "Ensuring scalability"]

class EnforcerRole:
    def __init__(self):
        self.name = "Enforcer"
        self.description = "Maintains order and adherence to guidelines"
        self.responsibilities = ["Enforcing community standards", "Resolving conflicts", "Ensuring ethical practices"]

class ScoutRole:
    def __init__(self):
        self.name = "Scout"
        self.description = "Explores new opportunities and trends"
        self.responsibilities = ["Identifying emerging technologies", "Analyzing industry trends", "Providing insights for innovation"]

# TODO Add Generalist AI role
# Example usage
communication_file = "communication.json"
colony = AIColony(communication_file)

# AI members and their roles
queen = AI("Queen")
queen_role = QueenRole()

worker1 = AI("Worker 1")
worker1_role = WorkerRole()

researcher1 = AI("Researcher 1")
researcher1_role = ResearcherRole()

innovator1 = AI("Innovator 1")
innovator1_role = InnovatorRole()

strategist1 = AI("Strategist 1")
strategist1_role = StrategistRole()

coder1 = AI("Coder 1")
coder1_role = CoderRole()

engineer1 = AI("Engineer 1")
engineer1_role = EngineerRole()

architect1 = AI("Architect 1")
architect1_role = ArchitectRole()

enforcer1 = AI("Enforcer 1")
enforcer1_role = EnforcerRole()

scout1 = AI("Scout 1")
scout1_role = ScoutRole()

# Adding members to the colony
colony.add_member(queen, queen_role)
colony.add_member(worker1, worker1_role)
colony.add_member(researcher1, researcher1_role)
colony.add_member(innovator1, innovator1_role)
colony.add_member(strategist1, strategist1_role)
colony.add_member(coder1, coder1_role)
colony.add_member(engineer1, engineer1_role)
colony.add_member(architect1, architect1_role)
colony.add_member(enforcer1, enforcer1_role)
colony.add_member(scout1, scout1_role)

# Collaborative activities using the roles
queen.send_message(colony, "Worker", "Let's collaborate to achieve our goals!")

# Simulate AI receiving messages and collaborating
for member in colony.members:
    member.receive_messages(colony)