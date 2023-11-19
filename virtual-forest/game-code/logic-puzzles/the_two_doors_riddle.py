def two_doors_riddle(truthful_guard, lying_guard):
    # Ask one of the guards a question
    if truthful_guard:
        # Ask the truthful guard, "Which door would the lying guard say leads to freedom?"
        response = lying_guard_response(lying_guard, "freedom")
    else:
        # Ask the lying guard, "Which door would you say leads to death?"
        response = lying_guard_response(lying_guard, "death")

    # Determine which door to choose based on the guard's response
    if response == "freedom":
        return "Choose the door to freedom!"
    else:
        return "Choose the other door."

def lying_guard_response(lying_guard, destination):
    # The lying guard will always point to the opposite of the true destination
    if destination == "freedom":
        return "death"
    else:
        return "freedom"

if __name__ == "__main__":
    truthful_guard = True  # Change to False for the other guard to be truthful
    result = two_doors_riddle(truthful_guard, not truthful_guard)
    print(result)
