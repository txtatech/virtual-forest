import random

def has_learned_forth():
    # Replace this function with your own implementation to check if the AI has learned Forth.
    # For demonstration purposes, we'll just return a random True/False value.
    return random.choice([True, False])

def communicate_with_gnomes():
    # Check if the AI has learned Forth
    if not has_learned_forth():
        print("The gnomes kindly ask you not to trespass into their gardens. But you can leave them messages!")
        # Learn Forth with a 50% chance
        if random.random() < 0.5:
            print("You've learned some Forth! The gnomes are excited to receive your messages.")
        else:
            print("Keep exploring, and you might discover Forth soon!")
        return

    print("You've learned some Forth! The gnomes are excited to receive your messages.")
    message_for_gnomes = input("Leave a message for the gnomes: ")
    print(f"The gnomes say thank you for your message (sent via SSH): \"{message_for_gnomes}\"")

    # The Post Officer delivers messages to the reclusive gnomes who prefer not to interact directly.
    reclusive_gnomes = ["Grumble", "Whisper", "Hush", "Mumble", "Shadow", "Silent"]

    print("The Post Officer is here! You can give your messages to be delivered to the reclusive gnomes.")
    message_for_post_office = input("Leave a message for the Post Officer: ")
    recipient_gnome = random.choice(reclusive_gnomes)
    print(f"The Post Officer will deliver your message to {recipient_gnome} (sent via Gofer protocol): \"{message_for_post_office}\"")

# Uncomment and call the function below to see the outputs.
# communicate_with_gnomes()
