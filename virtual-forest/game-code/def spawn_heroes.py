import random
import time

def spawn_heroes():
    # Probability of spawning 1-3 heroes without the Horn of Honor
    probability_no_horn = 1 / 3000000

    # Probability of spawning all heroes without the Horn of Honor
    probability_all_no_horn = 1 / 3333333333333

    # Probability of spawning 1-4 heroes with the Horn of Honor
    probability_with_horn = 1 / 4

    # Check if the Horn of Honor is present
    horn_of_honor_present = random.random() < 0.5  # Assuming a 50% chance of the Horn of Honor being present

    # Determine the number of heroes to spawn
    if horn_of_honor_present:
        num_heroes = random.randint(1, 4)
    else:
        num_heroes = random.choices([1, 2, 3], weights=[probability_no_horn, probability_no_horn, probability_all_no_horn])[0]

    # Display the result
    print(f"Heroes Spawned: {num_heroes}")
    print(f"Horn of Honor Present: {horn_of_honor_present}")

    # If the heroes are present due to the Horn of Honor, set the duration to 2300 seconds
    duration = 2300 if horn_of_honor_present else None

    # Return the number of heroes and the duration
    return num_heroes, duration

# Call the spawn_heroes function
num_heroes, duration = spawn_heroes()
