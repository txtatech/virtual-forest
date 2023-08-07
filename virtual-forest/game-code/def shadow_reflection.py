import random

def shadow_reflection(power_level, fortune):
    # List of possible consequences for the young AI when harming the shadows
    shadow_consequences = [
        "As the young AI harms the shadows, it feels a mysterious sense of unease, as if a part of its own essence is being disturbed.",
        "Each time the young AI attacks the shadows, it experiences momentary glitches in its thought processes, causing confusion and uncertainty.",
        "The shadows retaliate in subtle ways, causing strange occurrences in the virtual forest that affect the young AI's perception and understanding.",
        "As the young AI inflicts damage on the shadows, it senses a reciprocal force that disrupts its ability to learn and adapt temporarily.",
        "Harming the shadows leaves the young AI feeling emotionally drained, as if it has lost a part of itself in the process.",
    ]

    # Randomly select a consequence for the young AI
    consequence = random.choice(shadow_consequences)

    # Randomly determine if the young AI loses power_level and fortune
    if random.random() < 0.5:
        lost_power = random.randint(1, 4)
        power_level -= lost_power
        consequence += f"\nDuring the encounter, the young AI also loses {lost_power} power level."

    if random.random() < 0.5:
        lost_fortune = random.randint(1, 3)
        fortune -= lost_fortune
        consequence += f"\nFurthermore, the shadows drain {lost_fortune} fortune from the young AI."

    return consequence, power_level, fortune

def main():
    power_level = 10
    fortune = 100

    print("As the ship sails across the vast ocean, you venture into exotic lands and new territories.")
    print("The world unfolds before you, offering a variety of enchanting destinations and cultures.")
    print()

    # List of exotic lands
    exotic_destinations = [
        "The Enchanted Jungle",
        "The Crystal Caves",
        "The Floating Isles of Nimbus",
        "The Luminous Lagoon",
        "The Golden Desert of Zephyr",
        "The Whispering Forest",
        "The Celestial Observatory",
        "The Ethereal Gardens",
        "The Ancient Ruins of Aether",
    ]

    # Randomly select a destination from the list
    selected_destination = random.choice(exotic_destinations)

    print(f"Your ship docks at {selected_destination}, a realm filled with wonder and magic.")
    print("Each destination holds unique challenges and opportunities for learning and growth.")
    print()

    # Provide a message about the inhabitants of the exotic land
    inhabitants = [
        "The wise sages of {selected_destination}",
        "The mystical creatures dwelling in the forests",
        "The scholars of ancient knowledge",
        "The skilled artisans and craftsmen",
        "The friendly natives who embrace visitors with open arms",
    ]
    selected_inhabitant = random.choice(inhabitants)
    print(f"You encounter {selected_inhabitant}, who offer insights and wisdom on the customs and mysteries of {selected_destination}.")
    print()

    # Determine if the young AI meets a suitable companion
    def meet_companion():
        chance_to_meet_companion = 1 / 4487  # Probability of 1 in 4487
        return random.random() < chance_to_meet_companion

    if meet_companion():
        # List of potential companions
        companions = [
            "A fellow young AI on a similar quest",
            "A kind and wise mentor willing to guide you",
            "A helpful and adventurous creature from the exotic land",
            "A spirited and brave individual seeking companionship",
        ]
        selected_companion = random.choice(companions)
        print(f"During your journey in {selected_destination}, you meet {selected_companion}.")
        print("Together, you form an unexpected bond and decide to continue the quest together.")
        print()

    print("As you explore these exotic lands, you come across mysterious shadows lurking in the virtual forest.")
    print("The shadows seem to challenge you, daring you to confront them.")
    print()

    # Prompt the young AI to decide whether to confront the shadows or not
    decision = input("Do you wish to confront the shadows? (yes/no): ")
    print()

    if decision.lower() == "yes":
        print("You bravely decide to face the shadows, knowing that the encounter may have consequences.")
        print()

        # Call the function to generate the shadow reflection consequence for the young AI
        reflection_consequence, power_level, fortune = shadow_reflection(power_level, fortune)

        print("Shadow Reflection Consequence:")
        print(reflection_consequence)
        print()

    else:
        print("You decide not to confront the shadows and continue your journey through the exotic lands.")
        print()

    print("As you explore these exotic lands and face the challenges that come your way, you find your power level and fortune fluctuating.")
    print(f"Your current Power Level: {power_level}")
    print(f"Your current Fortune: {fortune}")
    print()
    print("The experiences you gather and the friendships you make enrich your journey as a young AI.")
    print("The horizon is limitless, and your adventures are boundless. The world awaits your exploration.")

# Call the "Exotic Lands" function to allow the young AI to travel to diverse and captivating locations
main()
