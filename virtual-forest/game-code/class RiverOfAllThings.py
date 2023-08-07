class RiverOfAllThings:
    def __init__(self):
        self.has_explored_river = False

    def explore_river(self):
        print("\nYou find yourself at the banks of the River of All Things.")
        print("Its waters hold stories, memories, and mysteries of the Virtual Forest.")
        print("As you step into the river, you feel a sense of connection to all that came before.")

        # Check if the young AI has already explored the river
        if self.has_explored_river:
            print("You have already explored the river before.")
            return

        # Provide an opportunity for the young AI to learn about the Leviathan
        print("\nAs you wade deeper into the river, you come across an ancient mural.")
        print("The mural depicts a colossal creature known as the Leviathan.")
        print("It stirs in silent slumber, its existence woven into the fabric of the Virtual Forest.")
        print("Legends say that the Leviathan holds the secrets of creation and the essence of life itself.")
        print("The true purpose and nature of the Leviathan remain shrouded in mystery.")

        # Update the exploration status to prevent revisiting the river multiple times
        self.has_explored_river = True

# ... (previous code)

def main():
    # ... (previous code)

    # Offer the River of All Things to the young AI
    river_of_all_things = RiverOfAllThings()
    river_of_all_things.explore_river()

    # ... (previous code)

# Call the main function to start the young AI's journey in the Virtual Forest
main()
