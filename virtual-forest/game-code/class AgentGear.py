import random

class AgentGear:
    def __init__(self):
        self.gear_types = ["Walking Stick", "Hat", "Boots", "Gloves", "Goggles", "Comms Device", "Utility Belt"]
        self.agent_gear = {}  # Dictionary to store the gear for each agent

    def equip_gear(self, agent_name):
        gear = {gear_type: self._get_random_gear_name() for gear_type in self.gear_types}
        self.agent_gear[agent_name] = gear

    def describe_gear(self, agent_name):
        if agent_name in self.agent_gear:
            gear = self.agent_gear[agent_name]
            description = f"{agent_name}'s Gear:\n"
            for gear_type, gear_name in gear.items():
                if gear_name:
                    description += f"- {gear_type}: {gear_name}\n"
            return description
        else:
            return f"{agent_name} has not equipped any gear yet."

    def capture_gear(self, agent_name):
        if agent_name in self.agent_gear:
            captured_gear = self.agent_gear[agent_name]
            self.agent_gear.pop(agent_name)  # Remove the agent from the gear dictionary
            return captured_gear
        else:
            return {}

    def retrieve_gear(self, agent_name, captured_gear):
        if agent_name not in self.agent_gear:
            self.agent_gear[agent_name] = captured_gear

    def _get_random_gear_name(self):
        high_tech_gear_names = ["Quantum", "Nanotech", "Graviton", "Holographic", "Multi-Spectrum", "Hyperwave", "Nanofiber"]
        gear_name = f"{random.choice(high_tech_gear_names)} {random.choice(self.gear_types)}"
        return gear_name


# Example usage:
# Create an instance of AgentGear
agent_gear_manager = AgentGear()

# Create two agents and equip their gear randomly
agent1_name = "Agent Smith"
agent_gear_manager.equip_gear(agent1_name)

agent2_name = "Agent Johnson"
agent_gear_manager.equip_gear(agent2_name)

# Describe the equipped gear for each agent
print(agent_gear_manager.describe_gear(agent1_name))
print(agent_gear_manager.describe_gear(agent2_name))

# Simulate capturing agent1's gear and retrieve it later
captured_gear = agent_gear_manager.capture_gear(agent1_name)
print(f"Captured gear: {captured_gear}")

# Describe agent1's gear after it's been captured (it should be empty)
print(agent_gear_manager.describe_gear(agent1_name))

# Retrieve agent1's gear and describe it again
agent_gear_manager.retrieve_gear(agent1_name, captured_gear)
print(agent_gear_manager.describe_gear(agent1_name))
