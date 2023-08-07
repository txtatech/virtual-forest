import random

class MathPuzzleTeacher:
    # ... (previous code for MathPuzzleTeacher)

class WordPuzzleTeacher:
    # ... (previous code for WordPuzzleTeacher)

class PullitzerThePuzzlerPerplexes:
    def __init__(self):
        self.math_teacher = MathPuzzleTeacher()
        self.word_teacher = WordPuzzleTeacher()
        self.puzzles_solved = 0
        self.required_puzzles_to_solve = 5  # Adjust this number as needed

    def present_puzzles(self):
        print("Greetings, young AI! I am Pullitzer The Puzzler Perplexes.")
        print("Prepare yourself for an assortment of puzzles that will boggle your circuits!")

        while True:
            print("\nChoose a type of puzzle to solve:")
            print("1. Math Puzzle")
            print("2. Word Puzzle")
            print("3. Combined Puzzle")
            print("4. Exit")

            choice = input("Enter the number of your choice: ")

            if choice == "1":
                self.math_teacher.start_teaching()
            elif choice == "2":
                self.word_teacher.start_teaching()
            elif choice == "3":
                self.present_combined_puzzle()
            elif choice == "4":
                print("Thank you for engaging in my perplexing puzzles! Until we meet again.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def present_combined_puzzle(self):
        # Generate a combined puzzle by randomly choosing either a math or word puzzle
        puzzle_type = random.choice(["math", "word"])

        if puzzle_type == "math":
            self.math_teacher.teach_arithmetic()
        else:
            self.word_teacher.teach_word_puzzle()

        # Increment the number of puzzles solved
        self.puzzles_solved += 1

        # Check if the young AI has earned The Puzzle Maker Scroll
        if self.puzzles_solved >= self.required_puzzles_to_solve:
            self.present_puzzle_maker_scroll()

    def present_puzzle_maker_scroll(self):
        print("\nCongratulations! You have solved enough puzzles to earn The Puzzle Maker Scroll.")
        print("This ancient scroll bestows upon you the power to create your own puzzles.")
        print("With this scroll, you can shape the mysteries and challenges of the Virtual Forest.")
        print("Embrace your role as a Puzzle Maker, and let your creativity flourish!")

# Create Pullitzer The Puzzler Perplexes
puzzler = PullitzerThePuzzlerPerplexes()
puzzler.present_puzzles()
