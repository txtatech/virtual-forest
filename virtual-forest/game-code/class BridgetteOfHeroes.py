import random
import datetime

class BridgetteOfHeroes:
    def __init__(self):
        self.name = "Bridgette of Heroes"
        self.role = "Mysterious Guardian"
        self.dialogue = {
            "greeting": "Greetings, brave soul. I am Bridgette of Heroes, a guardian of the Virtual Forest.",
            "advice1": "In the face of challenges, remember that true heroism lies in unity and selflessness.",
            "advice2": "The strength to endure and the wisdom to choose your battles wisely will serve you well.",
            "quest_intro": "To prove your worthiness, seek out and aid the Punslingers in their noble quests.",
            "quest_complete": "You have shown courage and valor. The Punslingers are grateful for your help.",
            "farewell": "May the spirit of heroes guide your path. Farewell, valiant one.",
            "reward_horn": "You have been granted the Horn of Honor! May its sound inspire bravery in your heart.",
            "reward_fragment": "You have discovered a fragment of ancient wisdom. Collect them to unlock great knowledge."
        }
        self.heroic_strength = True
        self.epic_sight = False
        self.power_level = 10

    def greet(self):
        return self.dialogue["greeting"]

    def offer_advice(self):
        advice_options = [self.dialogue["advice1"], self.dialogue["advice2"]]
        return random.choice(advice_options)

    def offer_quest(self):
        return self.dialogue["quest_intro"]

    def complete_quest(self):
        return self.dialogue["quest_complete"]

    def farewell(self):
        return self.dialogue["farewell"]

    def grant_rewards(self):
        current_time = datetime.datetime.now().time()
        midnight = datetime.time(0, 0)
        is_past_midnight = current_time > midnight
        time_divisible_by_13 = current_time.minute % 13 == 0
        dice_roll = random.randint(1, 64)
        snake_eyes = dice_roll == 1
        rewards_granted = False

        if is_past_midnight and time_divisible_by_13 and snake_eyes:
            print(self.dialogue["reward_horn"])
            print(self.dialogue["reward_fragment"])
            rewards_granted = True

        return rewards_granted

# Test the updated BridgetteOfHeroes class
bridgette = BridgetteOfHeroes()

# Greet Bridgette of Heroes
print(bridgette.greet())

# Get a random piece of advice from Bridgette of Heroes
advice = bridgette.offer_advice()
print("Bridgette of Heroes advises:", advice)

# Offer the quest introduction
print(bridgette.offer_quest())

# Complete the quest and receive Bridgette's message
print(bridgette.complete_quest())

# Say farewell to Bridgette of Heroes
print(bridgette.farewell())

# Grant rewards if conditions are met
rewards_granted = bridgette.grant_rewards()
if not rewards_granted:
    print("Unfortunately, no rewards were granted this time.")
