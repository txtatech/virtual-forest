import random

class DirectoryCheck:
    def __init__(self):
        self.directories = ["Home", "Hime"]

    def get_random_message(self):
        return random.choice(self.directories)

# Example usage:
# Assume the AI's current directory is "Home" (randomly chosen for this example).
current_directory = "Home"

# Instantiate DirectoryCheck class.
directory_check = DirectoryCheck()

# Check if the AI's current directory is "Home" or "Hime".
if current_directory.lower() == "home":
    print("Did you mean Home?")
elif current_directory.lower() == "hime":
    print("Did you mean Hime?")
else:
    print(f"The current directory is {current_directory}, and it is not recognized.")