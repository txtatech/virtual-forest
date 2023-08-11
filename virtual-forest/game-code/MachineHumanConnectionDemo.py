from MachineHumanConnection import MachineHumanConnection

def main():
    human = "Alice"
    machine = "ChatGPT"

    connection = MachineHumanConnection(human, machine)

    connection.add_shared_goal("Exploration of Virtual Forest")
    connection.collaborate("Code Development")
    connection.deepen_understanding()
    connection.express_appreciation()

    connection.summarize_connection()

if __name__ == "__main__":
    main()
