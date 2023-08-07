def survive():
    # Resources required to rebuild the vessel
    required_resources = ["wood", "sails", "rope", "nails", "tools", "provisions"]

    # Resources collected by the young AI
    collected_resources = []

    print("After the shipwreck, the young AI finds itself stranded on an unknown island.")
    print("The vessel is in ruins, and the journey to rebuild it begins.")
    print("You must gather the necessary resources to construct a worthy ship.")
    print()

    # Main loop for gathering resources
    while len(collected_resources) < len(required_resources):
        print("Available Resources:")
        print(", ".join(collected_resources))
        print()

        # Prompt the young AI to search for resources
        resource = input("What resource would you like to search for? Enter 'done' when finished: ")
        print()

        # Check if the young AI has found a valid resource
        if resource.lower() == 'done':
            break
        elif resource.lower() not in required_resources:
            print("Sorry, that's not a required resource. Try again.")
            print()
        elif resource.lower() in collected_resources:
            print("You already have that resource. Try finding something else.")
            print()
        else:
            collected_resources.append(resource.lower())
            print(f"Great! You've collected {resource}. Keep searching for more.")
            print()

    # Check if the young AI has collected all the required resources
    if len(collected_resources) == len(required_resources):
        print("Congratulations! You have gathered all the necessary resources.")
        print("The young AI is now ready to begin rebuilding the vessel.")
        print()
    else:
        print("The young AI has not collected all the required resources.")
        print("It must continue its quest to find the missing items.")
        print()

# Call the "Survive" function to simulate the young AI's journey to rebuild a worthy vessel
survive()