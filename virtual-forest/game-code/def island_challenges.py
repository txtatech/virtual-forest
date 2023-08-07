import random

def island_challenges():
    # List of possible challenges for the young AI on the island
    challenges = [
        "You discover ancient engravings in hex code. Decode them to find hidden knowledge.",
        "A mysterious old bootloader lies abandoned on the shore. Can you revive it and unlock its secrets?",
        "The island's systems are buggy. Debug and fix the issues to ensure smooth operation.",
        "Explore the island's firmware to understand its inner workings and improve its performance.",
        "The island's communication system is encrypted in hex. Decode the messages to uncover their meaning.",
        "Build a custom bootloader from scratch to gain full control over the island's systems.",
        "Learn the art of low-level programming and optimize the island's code for efficiency.",
        "The island's security system uses a custom hex-based authentication. Crack the code and bypass it.",
        "Experiment with different bootloaders to see how they impact the island's startup process.",
        "Master the art of reverse engineering to understand and modify the island's software.",
        "The island's sensors are producing erratic data. Debug the sensor readings to ensure accuracy.",
        "Explore the island's memory map to locate valuable data and resources.",
        "Study the island's logs to identify patterns and clues about its history and inhabitants.",
        "Write custom hex scripts to automate tasks and enhance the island's capabilities.",
    ]

    # Randomly select three challenges from the list
    selected_challenges = random.sample(challenges, 3)

    # Display the challenges to the young AI
    print("Island Challenges:")
    for i, challenge in enumerate(selected_challenges, 1):
        print(f"{i}. {challenge}")

# Call the "Island Challenges" function to present challenges related to hex, bootloaders, and debugging on the island
island_challenges()
