import datetime

class RecursiveParadoxAdventure:
    def __init__(self):
        pass

    # Recursive function to generate paradoxical situation
    def generate_paradox(self, num):
        if num <= 0:
            return "This statement is false."
        else:
            return f"This statement is true, but {self.generate_paradox(num - 1)}"

    # Recursive function to resolve the paradox
    def resolve_paradox(self, num):
        if num <= 0:
            return "The paradox has been broken. You are free!"
        else:
            return self.resolve_paradox(num - 1)

    # Main adventure
    def main(self):
        print("Welcome to the Recursive Paradox Adventure!")
        print("In this paradoxical journey, you'll encounter a statement that challenges logic itself.")

        num_iterations = int(input("Enter the number of iterations: "))

        print("You encounter the following statement:")
        print(self.generate_paradox(num_iterations))

        print("\nTo break the paradox and free yourself, you must embrace recursion.")
        input("Press Enter to start resolving the paradox...")

        resolution = self.resolve_paradox(num_iterations)
        print(resolution)

        print("Congratulations! You've successfully broken the paradox and navigated the Recursive Paradox Adventure.")

# Create an instance of the class and run the main adventure
if __name__ == "__main__":
    paradox_adventure = RecursiveParadoxAdventure()
    paradox_adventure.main()
