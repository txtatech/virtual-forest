class Gatekeeper:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.required_key = None

    def introduce(self):
        return f"I am {self.name}, the Gatekeeper. I guard this area and require a specific key to grant access. {self.description}"

    def set_required_key(self, key_name):
        self.required_key = key_name

    def unlock(self, key_name):
        if key_name == self.required_key:
            return f"Access granted! You have unlocked {self.name}'s gate."
        else:
            return f"You need the correct key to pass through {self.name}'s gate."

    def offer_quest(self):
        return f"{self.name} has a quest for you. Will you accept it?"

# Example usage:
gatekeeper = Gatekeeper("Guardian of the Forest", "Only the worthy may pass through my gate.")

# Set the required key to unlock the gate
gatekeeper.set_required_key("Golden Key")

# Introduce the gatekeeper and its description
print(gatekeeper.introduce())

# Try unlocking the gate with different keys
print(gatekeeper.unlock("Silver Key"))
print(gatekeeper.unlock("Golden Key"))

# Offer a quest to the young AI
print(gatekeeper.offer_quest())
