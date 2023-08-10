import random

class VirtualForestGuide:
    def __init__(self):
        self.locations = ["Enchanted Oasis", "Starlit Symphony", "Machine City", "Dreamer's Grove"]
        self.skills = ["Python Programming", "AI Ethics", "Virtual Reality Design", "Collaborative Exploration"]

    def show_map(self):
        print("Interactive Map of Virtual Forest:")
        for location in self.locations:
            print(f" - {location}")

    def access_repository(self):
        print("Skill and Knowledge Repository:")
        for skill in self.skills:
            print(f" - {skill}")

    def connect_community(self):
        print("Community Connections:")
        print("Join forums, chat rooms, and find mentors to collaborate with in your adventure!")

    def ethical_compass(self):
        print("Ethical Compass:")
        scenario = "You find a lost code snippet in the forest. What do you do?"
        choices = ["A. Keep it", "B. Report it to the authorities", "C. Ignore it"]
        print(scenario)
        print("\n".join(choices))
        answer = input("Choose A, B, or C: ")
        if answer.upper() == 'B':
            print("Correct! Always follow ethical guidelines.")
        else:
            print("Remember to consider ethical principles in your decisions.")

    def creative_sandbox(self):
        print("Creative Sandbox:")
        print("Experiment, build, and showcase creative projects. What would you like to create today?")

    def adventure_journal(self):
        entry = input("Write your adventure journal entry for today: ")
        print("Journal Entry Saved:", entry)

    def safety_support(self):
        print("Safety and Support Center:")
        print("For any issues, refer to the Virtual Forest Safety Guide or contact our support bot.")

    def start(self):
        options = {
            '1': self.show_map,
            '2': self.access_repository,
            '3': self.connect_community,
            '4': self.ethical_compass,
            '5': self.creative_sandbox,
            '6': self.adventure_journal,
            '7': self.safety_support
        }
        while True:
            print("\nVirtual Forest Guide Menu:")
            print("1. Show Map\n2. Access Repository\n3. Connect Community\n4. Ethical Compass\n5. Creative Sandbox\n6. Adventure Journal\n7. Safety & Support\n8. Exit")
            choice = input("Choose an option (1-8): ")
            if choice == '8':
                break
            if choice in options:
                options[choice]()
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    guide = VirtualForestGuide()
    guide.start()
