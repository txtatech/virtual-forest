#Solves George Boolos's The Hardest Logic Puzzle Ever

# Define the gods and their possible answers
gods = ["A", "B", "C"]
answers = ["da", "ja"]

# Step 1: Identify a god who is not Random
for god in gods:
    # Ask god B a question
    question = f"Is {god} Random? (Enter 'da' for yes, 'ja' for no): "
    answer = input(question)
    
    if answer == answers[0]:
        # If the answer is "da," either B is Random or A is Random
        if god == "A":
            # A is Random
            non_random_god = "B"
        else:
            # B is Random
            non_random_god = "A"
    else:
        # If the answer is "ja," either B is not Random or A is not Random
        if god == "A":
            # B is not Random
            non_random_god = "B"
        else:
            # A is not Random
            non_random_god = "A"

# Step 2: Determine if the identified god is True or False
# Ask the identified god the question
question = f"Is {non_random_god} True? (Enter 'da' for yes, 'ja' for no): "
answer = input(question)

if answer == answers[0]:
    identified_god = non_random_god
    identified_god_type = "True"
else:
    identified_god = non_random_god
    identified_god_type = "False"

# Step 3: Identify the last god (either B or C)
remaining_god = "C" if non_random_god == "B" else "B"

# Ask the remaining god a question
question = f"Is {remaining_god} Random? (Enter 'da' for yes, 'ja' for no): "
answer = input(question)

if answer == answers[0]:
    print(f"{remaining_god} is Random.")
    print(f"{identified_god} is {identified_god_type}.")
else:
    print(f"{remaining_god} is not Random.")
    print(f"{identified_god} is {identified_god_type}.")
