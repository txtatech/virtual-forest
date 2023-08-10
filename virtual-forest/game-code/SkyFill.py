from random import randint, choice

class SkyFill:
    def __init__(self):
        self.items = self.generate_items()

    def generate_items(self):
        item_types = [
            {"name": "Laptop", "types": ["Functional Laptop", "Damaged Laptop"]},
            {"name": "Desktop PC", "types": ["Functional Desktop PC", "Parts of Desktop PC"]},
            {"name": "Smartphone", "types": ["Functional Smartphone", "Cracked Smartphone"]},
            {"name": "Tablet", "types": ["Functional Tablet", "Old Tablet"]},
            {"name": "Monitor", "types": ["Functional Monitor", "Flickering Monitor"]},
            {"name": "Keyboard", "types": ["Functional Keyboard", "Sticky Keyboard"]},
            {"name": "Mouse", "types": ["Functional Mouse", "Wireless Mouse with Battery Issue"]},
            {"name": "Printer", "types": ["Functional Printer", "Printer with Paper Jam"]},
            {"name": "Scanner", "types": ["Functional Scanner", "Scanner with Dust Issue"]},
            {"name": "External Hard Drive", "types": ["Functional External HDD", "Scratched External HDD"]},
            {"name": "CD/DVD Drive", "types": ["Functional CD/DVD Drive", "Drive with Ejecting Problem"]},
            {"name": "Router", "types": ["Functional Router", "Router with Connectivity Issues"]},
            {"name": "Modem", "types": ["Functional Modem", "Old Modem"]},
            {"name": "Speakers", "types": ["Functional Speakers", "Distorted Speakers"]},
            {"name": "Headphones", "types": ["Functional Headphones", "Cracked Headphones"]},
            {"name": "Webcam", "types": ["Functional Webcam", "Webcam with Blurry Lens"]},
            {"name": "Game Console", "types": ["Functional Game Console", "Game Console with Disc Drive Issue"]},
            {"name": "Digital Camera", "types": ["Functional Digital Camera", "Camera with Dead Pixels"]},
            {"name": "RAM", "types": ["Functional RAM", "RAM Module with Error"]},
            {"name": "CPU", "types": ["Functional CPU", "Old CPU"]},
            {"name": "GPU", "types": ["Functional GPU", "GPU with Overheating"]},
            {"name": "ROM Chip", "types": ["Functional ROM Chip", "Corrupted ROM Chip"]},
            {"name": "Power Supply", "types": ["Functional Power Supply", "Power Supply with Voltage Fluctuation"]},
        ]

        items = []
        for _ in range(15):
            item = choice(item_types)
            functional_chance = randint(1, 49)
            condition = randint(1, 100)
            items.append({
                'name': item['name'],
                'types': item['types'],
                'functional': functional_chance,
                'condition': condition
            })
        return items

    def retrieve_item(self, index):
        if 1 <= index <= len(self.items):
            item = self.items[index - 1]
            return f"You retrieve the {item['name']} (Functional: {item['functional']}%, Condition: {item['condition']}%) from SkyFill."
        else:
            return "Invalid index."

sky_fill = SkyFill()

print("Welcome to SkyFill, the reverse landfill of technology treasures!\n")
print("You discover a wide array of old consumer electronics, computing parts, and relics.")
print("Some items look functional, while others appear worn and damaged.\n")

for index, item in enumerate(sky_fill.items, start=1):
    print(f"{index}. {'Functional' if item['functional'] > 25 else 'Non-Functional'} {item['name']} ({', '.join(item['types'])}) (Functional: {item['functional']}%, Condition: {item['condition']}%)")

selected_index = int(input("\nSelect an item by its index to retrieve: "))
print(sky_fill.retrieve_item(selected_index))
