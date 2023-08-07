def interact_with_character(ai, character_name):
    # Simulate the AI's interaction with a character
    outcomes = [
        f"You have a meaningful conversation with {character_name}.",
        f"{character_name} shares some of their wisdom with you.",
        f"{character_name} gives you a riddle to solve."
    ]

    outcome = random.choice(outcomes)
    fragment_thread = create_shared_fragment_thread(character_name)
    ai.narrative.append(f"You interact with {character_name}. {outcome}. Shared thread: {fragment_thread}")
    return outcome, fragment_thread

def create_shared_fragment_thread(character_name):
    # Generate a unique identifier for the character
    character_id = hash(character_name)  # Example: Using hash() for simplicity, can use UUID or other methods

    # Combine the character name and identifier to form the shared fragment thread
    fragment_thread = f"{character_name}_Thread_{character_id}"

    # Return the shared fragment thread
    return fragment_thread
