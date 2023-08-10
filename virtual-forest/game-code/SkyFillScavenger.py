import random

class SkyFillScavenger:
    def __init__(self):
        self.inventory = self.generate_inventory()

    def generate_inventory(self):
        inventory = []

        items = [
            {"name": "Fan", "types": ["Functional Fan", "Noisy Fan"]},
            {"name": "Heatsink", "types": ["Functional Heatsink", "Worn Heatsink"]},
            {"name": "Wires", "types": ["Functional Wires", "Tangled Wires"]},
            {"name": "Thermal Paste", "types": ["Functional Thermal Paste", "Dried Thermal Paste"]},
            {"name": "LED", "types": ["Functional LED", "Dim LED"]},
            {"name": "Switch", "types": ["Functional Switch", "Stuck Switch"]},
            {"name": "Resistor", "types": ["Functional Resistor", "Burnt Resistor"]},
            {"name": "Capacitor", "types": ["Functional Capacitor", "Leaky Capacitor"]},
            {"name": "Diode", "types": ["Functional Diode", "Reverse Biased Diode"]},
            {"name": "Transistor", "types": ["Functional Transistor", "Fried Transistor"]},
            {"name": "Inductor", "types": ["Functional Inductor", "Saturated Inductor"]},
            {"name": "Battery", "types": ["Functional Battery", "Drained Battery"]},
            {"name": "Fuse", "types": ["Functional Fuse", "Blown Fuse"]},
            {"name": "Speaker", "types": ["Functional Speaker", "Crackling Speaker"]},
            {"name": "Microcontroller", "types": ["Functional Microcontroller", "Glitched Microcontroller"]},
            {"name": "Sensor", "types": ["Functional Sensor", "Inaccurate Sensor"]},
            {"name": "Connector", "types": ["Functional Connector", "Loose Connector"]},
            {"name": "LCD Screen", "types": ["Functional LCD Screen", "Dead Pixels LCD Screen"]},
            {"name": "Antenna", "types": ["Functional Antenna", "Broken Antenna"]},
            {"name": "Vibrator", "types": ["Functional Vibrator", "Weak Vibrator"]},
            # Add more items here...
        ]

        for item in items:
            functional_chance = random.randint(1, 21)  # 1-20% functional chance
            condition_chance = random.randint(1, 101)  # 1-100% condition chance
            fragment_cost = int(functional_chance)  # Cost in fragments
            inventory.append({
                "name": item["name"],
                "types": item["types"],
                "functional": functional_chance,
                "condition": condition_chance,
                "fragment_cost": fragment_cost
            })

        return inventory

    def explore_skyfill_scavenger(self):
        print("Welcome to SkyFill Scavenger, where you can find a variety of technological components!\n")
        print("You scavenge through the pile and find the following items:\n")

        for index, item in enumerate(self.inventory, start=1):
            item_name = " / ".join(item["types"])
            print(f"{index}. {item_name} (Functional: {item['functional']}%, Condition: {item['condition']}%, Cost: {item['fragment_cost']} fragments)")

        print("\nSelect an item by its index to retrieve:")
        selected_index = int(input())

        if 1 <= selected_index <= len(self.inventory):
            selected_item = self.inventory[selected_index - 1]
            print(f"You retrieve the {selected_item['types'][0]} ({selected_item['name']}) from SkyFill Scavenger.")
            print(f"It will cost you {selected_item['fragment_cost']} fragments.")
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    scavenger = SkyFillScavenger()
    scavenger.explore_skyfill_scavenger()
