class BashScriptManager:
    def __init__(self):
        pass

    def show_all_bash_commands(self):
        bash_commands = show_bash_commands()
        return bash_commands

    def write_custom_bash_commands(self, custom_commands=[]):
        all_commands = write_bash_command(custom_commands)
        return all_commands
