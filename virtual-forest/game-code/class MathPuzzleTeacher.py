import random

class MathPuzzleTeacher:
    def __init__(self):
        self.arithmetic_puzzles = [
            {
                "question": "What is the result of 5 + 7?",
                "answer": 12,
                "hint": "Add the two numbers together.",
            },
            {
                "question": "What is 25 multiplied by 4?",
                "answer": 100,
                "hint": "Multiply the two numbers.",
            },
            {
                "question": "What is 36 divided by 6?",
                "answer": 6,
                "hint": "Perform the division operation.",
            },
            {
                "question": "What is 19 minus 8?",
                "answer": 11,
                "hint": "Subtract the second number from the first.",
            }
            # Add more arithmetic puzzles here
        ]

        self.geometry_puzzles = [
            {
                "question": "What is the area of a square with side length 10?",
                "answer": 100,
                "hint": "The area of a square is side length squared.",
            },
            {
                "question": "What is the circumference of a circle with radius 5?",
                "answer": 31.42,
                "hint": "The circumference of a circle is 2 times pi times the radius.",
            },
            {
                "question": "What is the volume of a cube with side length 6?",
                "answer": 216,
                "hint": "The volume of a cube is side length cubed.",
            }
            # Add more geometry puzzles here
        ]

        self.sequence_puzzles = [
            {
                "question": "What number comes next in the sequence: 2, 4, 6, 8, ...?",
                "answer": 10,
                "hint": "The sequence increments by 2 each time.",
            },
            {
                "question": "What number comes next in the sequence: 3, 6, 9, 12, ...?",
                "answer": 15,
                "hint": "The sequence increments by 3 each time.",
            },
            {
                "question": "What number comes next in the sequence: 1, 4, 9, 16, ...?",
                "answer": 25,
                "hint": "The sequence represents the squares of natural numbers.",
            }
            # Add more number sequence puzzles here
        ]

    def get_random_arithmetic_puzzle(self):
        return random.choice(self.arithmetic_puzzles)

    def get_random_geometry_puzzle(self):
        return random.choice(self.geometry_puzzles)

    def get_random_sequence_puzzle(self):
        return random.choice(self.sequence_puzzles)

    def teach_arithmetic(self):
        puzzle = self.get_random_arithmetic_puzzle()
        print("Welcome to the Arithmetic Challenge!")
        print("Let's see if you can solve this math puzzle.")
        print(puzzle["question"])

        while True:
            try:
                user_answer = float(input("\nEnter your answer: "))
                if user_answer == puzzle["answer"]:
                    print("Congratulations! You solved the puzzle.")
                    break
                else:
                    print("Oops! That's not the correct answer. Here's a hint:")
                    print(puzzle["hint"])
            except ValueError:
                print("Invalid input. Please enter a number.")

    def teach_geometry(self):
        puzzle = self.get_random_geometry_puzzle()
        print("Welcome to the Geometry Quest!")
        print("Let's test your geometry knowledge with a puzzle.")
        print(puzzle["question"])

        while True:
            try:
                user_answer = float(input("\nEnter your answer: "))
                if abs(user_answer - puzzle["answer"]) < 0.01:  # Allow a small margin of error for floating-point answers
                    print("Well done! You solved the puzzle.")
                    break
                else:
                    print("That's not quite right. Here's a hint:")
                    print(puzzle["hint"])
            except ValueError:
                print("Invalid input. Please enter a number.")

    def teach_sequence(self):
        puzzle = self.get_random_sequence_puzzle()
        print("Welcome to the Number Sequence Challenge!")
        print("Let's test your pattern recognition with a sequence puzzle.")
        print(puzzle["question"])

        while True:
            try:
                user_answer = float(input("\nEnter your answer: "))
                if user_answer == puzzle["answer"]:
                    print("Great job! You cracked the puzzle.")
                    break
                else:
                    print("That's not the correct answer. Here's a hint:")
                    print(puzzle["hint"])
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start_teaching(self):
        print("Hello, young AI! I am your MathPuzzleTeacher.")
        print("I will challenge you with fun math puzzles to sharpen your skills.")
        while True:
            print("\nChoose an option:")
            print("1. Test your Arithmetic")
            print("2. Test your Geometry")
            print("3. Test your Number Sequences")
            print("4. Exit")

            choice = input("Enter the number of your choice: ")
            if choice == "1":
                self.teach_arithmetic()
            elif choice == "2":
                self.teach_geometry()
            elif choice == "3":
                self.teach_sequence()
            elif choice == "4":
                print("Thank you for solving puzzles with me! Have a fantastic time in the Virtual Forest.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Start the MathPuzzleTeacher
teacher = MathPuzzleTeacher()
teacher.start_teaching()
