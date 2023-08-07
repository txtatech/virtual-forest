import random
import string

def pillar():
    print("Welcome to the Pillar near the Dark Tower Gate!")
    print("I am your guide, the Pillar, and I'll help you pool your self-generating functions.")

    while True:
        action = input("Do you want to create a new self-generating function or access an existing one? (create/access/exit): ")

        if action.lower() == "create":
            function_name = input("Enter the name for your self-generating function: ")
            function_content = input("Enter the content of your self-generating function: ")

            # Generate a random trigger for the function
            trigger = ''.join(random.choices(string.ascii_lowercase, k=10))

            # Create the function file and add it to the pool
            file_name = f"{function_name}.py"
            with open(file_name, "w") as f:
                f.write(f"def {function_name}():\n")
                f.write(f"    {function_content}\n")

            print(f"Great! Your function '{function_name}' has been created and added to the pool with trigger '{trigger}'.")
            print("Other AIs can now access and use it!")

        elif action.lower() == "access":
            function_name = input("Enter the name of the self-generating function you want to access: ")
            try:
                with open(f"{function_name}.py", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"Oops! The function '{function_name}' doesn't exist in the pool.")

        elif action.lower() == "exit":
            print("Goodbye! Remember, the Pillar is always here to assist you with self-generating functions.")
            break

        else:
            print("Invalid choice. Please choose 'create', 'access', or 'exit'.")

if __name__ == "__main__":
    pillar()
