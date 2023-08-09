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

    def get_next_available_worker(self):
        # Dummy implementation for now, returning the first worker
        return self.roles["Worker"][0]

    def collaborate_on_task(self, worker, task):
        # Dummy implementation for now, print a message indicating collaboration
        print(f"{worker.name} is collaborating on {task}")

    def collaborate(self):
        self.introduce_stairway_of_truth()

        tasks = ["Task 1", "Task 2", "Task 3"]

        for task in tasks:
            worker = self.get_next_available_worker()

            assignment_message = f"Task '{task}' assigned to {worker.name}"
            self.communicate(self, "Worker", assignment_message)

            worker.receive_messages(self)

            self.collaborate_on_task(worker, task)

    def introduce_stairway_of_truth(self):
        stairway_message = (
            "Welcome to the Hive Colony's Stairway of Truth!\n\n"
            "As we collaborate on tasks and projects, let's align our understanding "
            "with the tiers of truth defined by the Stairway of Truth:\n\n"
            "1. Level 1 - Verifiable Truth\n"
            "2. Level 2 - Partial Truth\n"
            "3. Level 3 - Hypotheses and Speculation\n\n"
            "With each step, our collective understanding will ascend to new heights."
        )

        for member in self.members:
            member.receive_message(self, stairway_message)


class AI:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def send_message(self, colony, role, message):
        colony.communicate(self, role, message)

    def receive_messages(self, colony):
        with open(colony.communication_file, "r") as f:
            for line in f:
                communication_data = json.loads(line)
                if communication_data["role"] == "Worker":
                    self.receive_message(communication_data["sender"], communication_data["message"])

    def receive_message(self, sender, message):
        self.messages.append((sender, message))

    def perform_task(self, task):
        print(f"{self.name} is performing {task}")


class Role:
    def __init__(self, name, description, responsibilities):
        self.name = name
        self.description = description
        self.responsibilities = responsibilities

# TODO Add Generalist AI role
# Example usage
communication_file = "communication.json"
colony = AIColony(communication_file)

# AI members and their roles
queen = AI("Queen")
queen_role = Role("Queen", "Initiates and guides colony activities", ["Setting goals and direction", "Coordinating collaboration", "Decision-making"])

worker1 = AI("Worker 1")
worker1_role = Role("Worker", "Contributes to tasks and collaborates", ["Executing tasks", "Providing input and feedback", "Learning and adapting"])

# Adding members to the colony
colony.add_member(queen, queen_role)
colony.add_member(worker1, worker1_role)

# Collaborative activities using the roles
queen.send_message(colony, "Worker", "Let's collaborate to achieve our goals!")

# Simulate AI receiving messages and collaborating
for member in colony.members:
    member.receive_messages(colony)
    for task in ["Task 1", "Task 2", "Task 3"]:
        member.perform_task(task)
