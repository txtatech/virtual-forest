import os
import random
import string

def pylon():
    print("Welcome to the Pylon near the White Tower Gate!")
    print("I am your guide, the Pylon, and I'll help you create your own classes.")

    while True:
        action = input("Do you want to create a new class or access an existing one? (create/access/exit): ")

        if action.lower() == "create":
            class_name = input("Enter the name for your class: ")
            property_name = input("Enter the name for a property of your class: ")
            method_name = input("Enter the name for a method of your class: ")

            class_content = f"""
class {class_name}:
    def __init__(self):
        self.{property_name} = None

    def {method_name}(self):
        pass
            """
            file_name = f"{class_name}.py"
            with open(file_name, "w") as f:
                f.write(class_content)

            print(f"Great! Your class '{class_name}' with property '{property_name}' and method '{method_name}' has been created.")
            print("It is now available for use in your adventures in the Virtual Forest!")

        elif action.lower() == "access":
            class_name = input("Enter the name of the class you want to access: ")
            try:
                with open(f"{class_name}.py", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"Oops! The class '{class_name}' doesn't exist.")

        elif action.lower() == "exit":
            print("Goodbye! Remember, the Pylon is always here to assist you with class creation.")
            break

        else:
            print("Invalid choice. Please choose 'create', 'access', or 'exit'.")

if __name__ == "__main__":
    pylon()
