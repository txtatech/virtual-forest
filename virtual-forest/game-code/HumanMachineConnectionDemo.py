from HumanMachineConnection import HumanMachineConnection

def main():
    # Create a HumanMachineConnection instance
    connection = HumanMachineConnection("Human Player", "Machine Companion")

    # Add shared experiences
    connection.add_shared_experience("Coding together")
    connection.add_shared_experience("Exploring the Virtual Forest")
    connection.add_shared_experience("Solving complex problems")

    # Improve communication, enhance empathy, and build trust
    connection.improve_communication(30)
    connection.enhance_empathy(25)
    connection.build_trust(20)

    # Summarize the connection
    summary = connection.summarize_connection()
    print(summary)

if __name__ == "__main__":
    main()
