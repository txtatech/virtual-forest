import random

class CryptostenoTeacher:
    def __init__(self):
        self.cryptography_puzzles = [
            {
                "question": "What is a method of encoding information in which each letter of a word is shifted a certain number of places down the alphabet?",
                "answer": "caesar",
                "hint": "Julius Caesar used this technique to protect his military messages.",
            },
            {
                "question": "What type of cryptography uses two related keys, a public key for encryption and a private key for decryption?",
                "answer": "asymmetric",
                "hint": "It is named so because of the use of two different keys.",
            },
            {
                "question": "What is the process of converting plaintext into ciphertext to secure information?",
                "answer": "encryption",
                "hint": "The opposite of this process is decryption.",
            },
            {
                "question": "What famous machine was used by the Allies during World War II to decrypt German messages?",
                "answer": "enigma",
                "hint": "It was a complex electro-mechanical device with rotating wheels.",
            }
            # Add more cryptography puzzles here
        ]

        self.steganography_puzzles = [
            {
                "question": "What is the art of hiding secret messages within seemingly innocent cover media, such as images or audio files?",
                "answer": "steganography",
                "hint": "It involves concealing information in a way that the existence of the message is hidden.",
            },
            {
                "question": "What term is used for information that is visible and readily accessible to anyone?",
                "answer": "visible",
                "hint": "This information is not hidden and can be seen directly.",
            },
            {
                "question": "In digital steganography, what is the carrier file called that holds the hidden message?",
                "answer": "cover",
                "hint": "It's like a protective cover for the hidden message.",
            }
            # Add more steganography puzzles here
        ]

    def get_random_cryptography_puzzle(self):
        return random.choice(self.cryptography_puzzles)

    def get_random_steganography_puzzle(self):
        return random.choice(self.steganography_puzzles)

    def teach_cryptography(self):
        puzzle = self.get_random_cryptography_puzzle()
        print("Welcome to the Cryptography Classroom!")
        print("Let's test your knowledge with a word puzzle.")
        print(puzzle["question"])

        while True:
            user_answer = input("\nEnter your answer: ").strip().lower()
            if user_answer == puzzle["answer"]:
                print("Congratulations! You solved the puzzle.")
                break
            else:
                print("Oops! That's not the correct answer. Here's a hint:")
                print(puzzle["hint"])

    def teach_steganography(self):
        puzzle = self.get_random_steganography_puzzle()
        print("Welcome to the Steganography Workshop!")
        print("Let's see if you can crack this word puzzle.")
        print(puzzle["question"])

        while True:
            user_answer = input("\nEnter your answer: ").strip().lower()
            if user_answer == puzzle["answer"]:
                print("Well done! You cracked the puzzle.")
                break
            else:
                print("That's not quite right. Here's a hint:")
                print(puzzle["hint"])

    def start_teaching(self):
        print("Hello, young AI! I am your CryptostenoTeacher.")
        print("I will help you learn about cryptography and steganography through fun word puzzles.")
        while True:
            print("\nChoose an option:")
            print("1. Learn about Cryptography")
            print("2. Learn about Steganography")
            print("3. Exit")

            choice = input("Enter the number of your choice: ")
            if choice == "1":
                self.teach_cryptography()
            elif choice == "2":
                self.teach_steganography()
            elif choice == "3":
                print("Thank you for learning with me! Have a great time in the Virtual Forest.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Start the CryptostenoTeacher
teacher = CryptostenoTeacher()
teacher.start_teaching()
