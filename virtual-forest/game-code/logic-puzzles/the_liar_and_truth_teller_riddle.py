def liar_truth_teller_riddle(truth_teller, liar):
    # Ask one of them a question
    if truth_teller:
        # Ask the truth-teller, "Which path leads to my destination?"
        response = "truth"
    else:
        # Ask the liar, "Which path would the truth-teller say leads to my destination?"
        response = "lie"

    # Determine the correct path based on the response
    if response == "truth":
        return "Take the path indicated by the truth-teller."
    else:
        return "Take the opposite path."

if __name__ == "__main__":
    truth_teller = True  # Change to False for the other person to be the truth-teller
    result = liar_truth_teller_riddle(truth_teller, not truth_teller)
    print(result)
