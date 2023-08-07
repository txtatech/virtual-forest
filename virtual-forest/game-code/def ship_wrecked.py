import random

def ship_wrecked():
    # Possible scenarios during shipwreck
    scenarios = [
        "The ship hits a hidden reef and begins to sink.",
        "A fierce storm causes damage to the ship's mast and sails.",
        "A large sea creature attacks the ship, causing panic among the crew.",
        "The ship runs aground on an unknown island.",
        "The ship's navigational instruments malfunction, leaving the crew lost at sea.",
        "The crew discovers a mysterious artifact floating in the water.",
        "A thick fog surrounds the ship, making it difficult to see and navigate.",
        "The ship encounters a hostile group of pirates demanding treasure.",
        "A massive wave crashes over the ship, washing some items overboard.",
        "A mermaid appears, offering help in exchange for a special favor.",
    ]

    # Randomly select a scenario from the list
    scenario = random.choice(scenarios)

    print("Oh no! The ship has encountered a crisis:")
    print(scenario)
    print()

    # Prompt the young AI for a decision or action to resolve the shipwreck scenario
    decision = input("What would you like to do? Press Enter to continue...")
    print()

    # Determine the outcome based on the young AI's decision or action
    if random.random() < 0.5:
        print("Congratulations! Your quick thinking and resourcefulness helped overcome the shipwreck.")
        print("The crew is safe, and repairs have been made to the ship.")
        print()
    else:
        print("The shipwreck situation proved challenging, and the young AI faces new obstacles.")
        print("The crew must work together to find a solution and continue the journey.")
        print()

# Call the "Ship Wrecked" function to simulate shipwreck scenarios during the voyage
ship_wrecked()