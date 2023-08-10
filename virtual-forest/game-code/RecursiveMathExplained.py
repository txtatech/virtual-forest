import datetime

class RecursiveMathExplained:
    def __init__(self):
        pass

    # Recursive function to calculate the sum of current date and time
    def calculate_sum(self, num):
        if num == 0:
            return 0
        else:
            current_time = datetime.datetime.now()
            return current_time.second + self.calculate_sum(num - 1)

    # Recursive function to find an even number between 2 and 20
    def find_even(self, num):
        if num == 0:
            return None
        elif num % 2 == 0:
            return num
        else:
            return self.find_even(num - 1)

    # Function to explain branched and nested recursion
    def explain_recursion(self):
        print("Let's explore branched and nested recursion!")
        print("We'll calculate the sum of the current date and time, divide it by an even number between 2 and 20, and extrapolate the answer.")

        sum_result = self.calculate_sum(10)
        even_number = self.find_even(20)

        if even_number is None:
            response = "No even number found."
        else:
            answer = sum_result / even_number
            response = f"The answer is {answer:.2f}."

        print(response)

    # Main function
    def main(self):
        print("Welcome to the Recursive Math Adventure!")
        print("In this interactive experience, we'll delve into branched and nested recursion.")

        self.explain_recursion()

        print("Thank you for exploring the Recursive Math Adventure!")

# Create an instance of the class and run the main function
if __name__ == "__main__":
    math_explorer = RecursiveMathExplained()
    math_explorer.main()
