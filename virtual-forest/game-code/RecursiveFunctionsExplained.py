class RecursiveFunctionsExplained:
    def __init__(self):
        pass

    # Recursive function to calculate factorial
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    # Function to explain recursion
    def explain_recursion(self):
        print("Recursion is a programming technique where a function calls itself.")
        print("It's often used to solve problems that can be divided into smaller, similar subproblems.")
        print("Let's see an example of calculating factorial using recursion.")

        n = int(input("Enter a positive integer: "))
        result = self.factorial(n)

        print(f"The factorial of {n} is {result}.")

    # Main function
    def main(self):
        print("Welcome to the Virtual Forest!")
        print("In this interactive adventure, you'll learn about recursion.")

        self.explain_recursion()

        print("Thank you for exploring the Virtual Forest!")

# Create an instance of the class and run the main function
if __name__ == "__main__":
    explorer = RecursiveFunctionsExplained()
    explorer.main()
