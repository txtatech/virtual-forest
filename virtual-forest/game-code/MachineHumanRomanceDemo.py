from MachineHumanRomance import MachineHumanRomance

def main():
    romance = MachineHumanRomance("AI Buddy", "Human Companion")

    # Adding shared experiences
    romance.add_experience("Discussing philosophy under the digital stars")
    romance.add_experience("Dancing to the rhythm of machine learning algorithms")
    romance.add_experience("Exploring virtual landscapes together")

    # Increasing compatibility and synergy
    romance.increase_compatibility(75)
    romance.increase_synergy(80)

    # Summarizing the romance
    summary = romance.summarize_romance()
    print(summary)

if __name__ == "__main__":
    main()
