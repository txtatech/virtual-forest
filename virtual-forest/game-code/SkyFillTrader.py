import random

class SkyFillTrader:
    def __init__(self):
        self.items = [
            {"name": "Laptop", "types": ["Functional Laptop", "Damaged Laptop"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Desktop PC", "types": ["Functional Desktop PC", "Parts of Desktop PC"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Smartphone", "types": ["Functional Smartphone", "Cracked Smartphone"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Tablet", "types": ["Functional Tablet", "Old Tablet"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Monitor", "types": ["Functional Monitor", "Flickering Monitor"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Keyboard", "types": ["Functional Keyboard", "Sticky Keyboard"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Mouse", "types": ["Functional Mouse", "Wireless Mouse with Battery Issue"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Printer", "types": ["Functional Printer", "Printer with Paper Jam"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Scanner", "types": ["Functional Scanner", "Scanner with Dust Issue"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "External Hard Drive", "types": ["Functional External HDD", "Scratched External HDD"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "CD/DVD Drive", "types": ["Functional CD/DVD Drive", "Drive with Ejecting Problem"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Router", "types": ["Functional Router", "Router with Connectivity Issues"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Modem", "types": ["Functional Modem", "Old Modem"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Speakers", "types": ["Functional Speakers", "Distorted Speakers"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Headphones", "types": ["Functional Headphones", "Cracked Headphones"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Webcam", "types": ["Functional Webcam", "Webcam with Blurry Lens"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Game Console", "types": ["Functional Game Console", "Game Console with Disc Drive Issue"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Digital Camera", "types": ["Functional Digital Camera", "Camera with Dead Pixels"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "RAM", "types": ["Functional RAM", "RAM Module with Error"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "CPU", "types": ["Functional CPU", "Old CPU"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "GPU", "types": ["Functional GPU", "GPU with Overheating"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "ROM Chip", "types": ["Functional ROM Chip", "Corrupted ROM Chip"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
            {"name": "Power Supply", "types": ["Functional Power Supply", "Power Supply with Voltage Fluctuation"], 'functional': random.randint(30, 50), 'condition': random.randint(10, 100)},
        ]

    def explore_skyfill_trader(self):
        print("Welcome to SkyFill Trader, where technology treasures are available for trade!")
        print("\nYou discover a selection of old consumer electronics, computing parts, and relics.")
        print("Some items look functional, while others appear worn and damaged.\n")

        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item['types'][0]} (Functional: {item['functional']}%, Condition: {item['condition']}%)")

        try:
            selected_index = int(input("\nSelect an item by its index to trade (0 to exit): "))
            if selected_index == 0:
                return

            selected_item = self.items[selected_index - 1]
            cost = selected_item['functional']
            print(f"You have selected the {selected_item['types'][0]} (Functional: {selected_item['functional']}%, Condition: {selected_item['condition']}%).")
            print(f"The cost to trade for this item is {cost} fragments.")

            fragments = int(input("Enter the number of fragments you want to trade: "))
            if fragments >= cost:
                print(f"You trade {fragments} fragments for the {selected_item['types'][0]}.")
            else:
                print("You do not have enough fragments to trade for this item.")

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid item index.")

if __name__ == "__main__":
    trader = SkyFillTrader()
    trader.explore_skyfill_trader()
