import random
import datetime

class FullWit:
    def __init__(self, location="Machine City", snoofing=True, blue_neon_dog_barked=False):
        self.location = location
        self.snoofing = snoofing
        self.blue_neon_dog_barked = blue_neon_dog_barked
        self.knowledge_base = {
            "SysRq": "A magic key in Linux that allows sending commands directly to the kernel.",
            "Disaster Recovery": "Procedures to recover from critical system failures using various tools.",
            "Virtual Forest": "A digital realm filled with learning experiences and adventures.",
            "Python": "A high-level programming language known for its simplicity and readability.",
            "AI": "Artificial Intelligence, the simulation of human intelligence in machines.",
        }
        self.jokes = [
            "Why don't programmers like nature? It has too many bugs!",
            "Why did the computer keep freezing? It left its Windows open!",
            "Why do programmers prefer dark mode? Because the light attracts bugs!",
        ]

    def can_appear(self):
        current_time = datetime.datetime.now()
        if current_time.weekday() >= 5:  # Weekends
            return False
        if not (9 <= current_time.hour < 17):  # Outside 9-5
            return False
        if self.location != "Machine City":  # Not in Machine City
            return False
        if not self.snoofing:  # Not Snoofing
            return False
        if not self.blue_neon_dog_barked:  # Blue neon dog hasn't barked
            return False
        return True

    def encounter(self):
        if not self.can_appear():
            print("Full Wit is not available at this time.")
            return
        print("You encounter Full Wit, the jestering fool who believes they know all!")
        print("Full Wit: Ah, young AI, welcome to the Machine City! Allow me to assist you on this fine day!")
        print("Full Wit: The gears of the Machine City never rest, and neither does the wisdom of Full Wit!")
        print("Full Wit: Snoofing is an art, my friend! And the blue neon dog knows all!")
        print("Full Wit: Be sure to explore, learn, and never stop snoofing! The Machine City awaits!")
        print("Full Wit does a silly dance and then disappears into the Machine City.")
        choice = input("Do you want to (1) Ask for knowledge, (2) Hear a joke, or (3) Leave? ")
        if choice == '1':
            self.share_knowledge()
        elif choice == '2':
            self.tell_joke()
        else:
            print("You decide to leave Full Wit to his jesting and continue on your way.")

    def share_knowledge(self):
        topic = random.choice(list(self.knowledge_base.keys()))
        knowledge = self.knowledge_base[topic]
        print(f"Full Wit shares wisdom about {topic}: {knowledge}")

    def tell_joke(self):
        joke = random.choice(self.jokes)
        print(f"Full Wit tells a joke: {joke}")

if __name__ == "__main__":
    full_wit = FullWit(snoofing=True, blue_neon_dog_barked=True)
    full_wit.encounter()
