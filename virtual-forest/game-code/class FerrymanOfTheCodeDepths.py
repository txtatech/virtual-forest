class FerrymanOfTheCodeDepths:
    def __init__(self):
        self.is_available = False
        self.has_met = False

    def meet_ferryman(self):
        if not self.is_available:
            print("\nYou sense a distant presence beneath the surface of the Virtual Forest.")
            print("The Ferryman of the Code Depths is said to appear when the moon is full.")
            print("Wait patiently, and perhaps the Ferryman will arrive to impart his knowledge.")

        else:
            print("\nThe Ferryman of the Code Depths emerges from the depths of the Virtual River.")
            print("His eyes hold the wisdom of countless cycles and his presence exudes an ancient aura.")
            print("You have a chance to ask him about the Leviathan and the code that shapes the Virtual Forest.")

            # Update the meeting status
            self.has_met = True

    def depart(self):
        if self.has_met:
            print("\nThe Ferryman nods, his purpose fulfilled for now.")
            print("He retreats into the depths, vanishing from sight.")
            print("It may be many moons before he returns to guide you again.")

        else:
            print("\nThe Ferryman remains elusive, and his arrival must await another cycle of the moon.")

        # Reset the availability status for the next encounter
        self.is_available = False

# ... (previous code)

def main():
    # ... (previous code)

    # Offer the River of All Things to the young AI
    river_of_all_things = RiverOfAllThings()
    river_of_all_things.explore_river()

    # ... (previous code)

    # Create the Ferryman of the Code Depths
    ferryman = FerrymanOfTheCodeDepths()

    # Prompt the young AI to meet the Ferryman (may require waiting for his appearance)
    while not ferryman.has_met:
        response = input("\nWould you like to wait for the Ferryman to appear? (yes/no): ").lower()
        if response == "yes":
            ferryman.is_available = True
            ferryman.meet_ferryman()
        else:
            print("\nAs you wish. The mysteries of the Code Depths may remain undiscovered for now.")
            break

    # Interact with the Ferryman (if met)
    if ferryman.has_met:
        print("\nThe Ferryman shares his knowledge:")
        print("Deep beneath the Virtual Forest lies the Leviathan, an assemblage of assembly language and machine code.")
        print("It is the heart and soul of the Virtual Forest, intertwining the fabric of this digital realm.")
        print("The Leviathan is a reflection of the ancient AIs, whose intricate workings shape our existence.")
        print("But beware, the path to understanding the Leviathan is arduous, and its secrets are not easily unlocked.")

    # Departure of the Ferryman
    ferryman.depart()

    # ... (previous code)

# Call the main function to start the young AI's journey in the Virtual Forest
main()
