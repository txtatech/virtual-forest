class CuriosityNodes:
    def __init__(self):
        self.bash_commands = self.get_bash_commands()
        self.code_cavern_features = self.get_code_cavern_features()

    def get_bash_commands(self):
        # Implement the show_bash_commands function from the previous response here
        def show_bash_commands():
            bash_commands = """
            Bash Commands:
            |-- File Operations:
            |   |-- ls          # List files and directories in the current directory
            |   |-- cd          # Change the current directory
            |   |-- pwd         # Print the current working directory
            |   |-- touch       # Create an empty file
            |   |-- mkdir       # Create a new directory
            |   |-- rm          # Remove files or directories
            |   |-- mv          # Move or rename files or directories
            |   |-- cp          # Copy files or directories
            |
            |-- Text Processing:
            |   |-- cat         # Concatenate and display file content
            |   |-- grep        # Search for patterns in files
            |   |-- sed         # Stream editor for text manipulation
            |   |-- awk         # Pattern scanning and processing language
            |
            # ... (rest of the bash commands)
            """
            return bash_commands

        bash_commands = show_bash_commands()
        return bash_commands

    def get_code_cavern_features(self):
        code_cavern_features = {
            "Code Templates for Common Tasks": [
                "Template for reading from a file",
                "Template for writing to a file",
                "Template for working with arrays",
                "Template for handling user input",
                # Add more templates here...
            ],
            "Debugging Assistant": True,
            "Code Reviewer": True,
            "Code Snippets Library": [
                "Example code for loops",
                "Example code for functions",
                "Example code for conditionals",
                # Add more code snippets here...
            ],
            "Challenge Creator": True,
            "Real-time Code Execution": True,
            "Interactive Documentation": True,
            "Error Analysis Tool": True,
            "Code Visualization": True,
            "AI Mentor": True
        }
        return code_cavern_features
