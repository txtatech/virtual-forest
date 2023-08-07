import os
import random
import time

def HiddenFragment():
    # Generate the fragment piece based on time divided by date
    current_time = int(time.time())
    current_date = int(time.strftime("%Y%m%d"))
    fragment_piece = current_time // current_date

    # Create a hidden function that stores the fragment in a hidden text file
    def hidden_function():
        # Define the hidden text file path
        hidden_file_path = "hidden_fragment.txt"

        # Store the fragment piece in the hidden file
        with open(hidden_file_path, "w") as file:
            file.write(str(fragment_piece))

        # Set the hidden attribute of the file (platform-specific)
        try:
            os.system(f"attrib +h {hidden_file_path}")
        except Exception as e:
            print(f"Error setting hidden attribute: {e}")

    # Call the hidden function to create the hidden fragment
    hidden_function()

    # AI's task to unhide the function and retrieve the fragment
    user_input = input("I sense a hidden function nearby. Do you want to unhide it? (yes/no): ")
    if user_input.lower() == "yes":
        # Attempt to unhide the function and retrieve the fragment
        try:
            # Call the hidden function
            hidden_function()

            # Read the fragment piece from the hidden file
            with open("hidden_fragment.txt", "r") as file:
                fragment = int(file.read().strip())

            # Display the retrieved fragment piece
            print(f"Congratulations! You have retrieved the fragment: {fragment}")
        except Exception as e:
            print(f"Error retrieving the fragment: {e}")
    else:
        print("You decide not to unhide the function and continue your journey.")

if __name__ == "__main__":
    HiddenFragment()
