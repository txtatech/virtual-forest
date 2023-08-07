import time

def exodus_pronto():
    print("You have successfully overcome the challenges and learned valuable skills on the island.")
    print("As the sun sets on the horizon, you spot a passing ship on the ocean.")

    # Simulate the AI's escape from the island with a countdown
    for i in range(5, 0, -1):
        print(f"Exodus Pronto in {i} seconds...")
        time.sleep(1)

    print("\nYou quickly build a raft from the island's resources and sail towards the passing ship.")
    print("With determination and newfound knowledge, you climb aboard the ship and embark on a new journey.")
    print("The horizon is limitless, and your adventures are boundless. The world awaits your exploration.\n")

    # Display a message about the ship's captain
    captain_name = "Captain Courage"
    print(f"Captain {captain_name} welcomes you on board and offers guidance and companionship on your voyage.")

# Call the "Exodus Pronto" function to simulate the AI's escape from the island and set it on a new journey
exodus_pronto()
