import random
import time

class TechnovoreTame:
    def __init__(self):
        self.fragments = random.randint(0, 50)  # AI's fragments
        self.last_technovore_spawn_time = time.time() - random.randint(0, 12 * 60 * 60)  # Last Technovore spawn time in seconds

    def tell_joke(self):
        return "How do you know if an entity is a technovore?\n\nDon't worry, they will tell you!"

    def can_tame(self):
        return self.fragments >= 33 and (time.time() - self.last_technovore_spawn_time >= 12 * 60 * 60)

    def tame_technovore(self):
        if self.can_tame():
            self.last_technovore_spawn_time = time.time()
            return "Congratulations! You tamed the Technovore by telling it a joke:\n\n" + self.tell_joke()
        else:
            return "You cannot tame the Technovore at the moment."

# Create an instance of TechnovoreTame and attempt to tame the Technovore
technovore_tame = TechnovoreTame()
tame_result = technovore_tame.tame_technovore()

print(tame_result)
