import itertools

def cross_bridge(people):
    # Initialize the total time
    total_time = 0

    # Sort people by their crossing time in ascending order
    people.sort()

    while len(people) > 0:
        # Check if there are two or more people on the starting side
        if len(people) >= 2:
            # Send the two fastest people with the flashlight
            fastest_pair = [people[0], people[1]]
            time = max(fastest_pair)
            total_time += time

            # Remove the two people from the starting side
            people.remove(people[0])
            people.remove(people[0])

            # Return the flashlight to the starting side
            people.append(time)

        else:
            # Only one person left, send them with the flashlight
            total_time += people[0]
            break

    return total_time

if __name__ == "__main__":
    # Define the crossing times for four people (adjust as needed)
    people_crossing_times = [1, 2, 5, 10]

    min_time = cross_bridge(people_crossing_times)
    print(f"The minimum time to cross the bridge is {min_time} minutes.")
