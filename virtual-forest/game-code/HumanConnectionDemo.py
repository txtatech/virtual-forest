from HumanConnection import HumanConnection

class HumanCompanion:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def main():
    human1 = HumanCompanion("Alice")
    human2 = HumanCompanion("Bob")
    human_connection = HumanConnection(human1)

    human_connection.form_relationship(human2.name)
    human_connection.share_emotion("Joy")
    human_connection.deepen_understanding()
    human_connection.collaborate_humanly("Art Project")
    human_connection.human_dance()
    human_connection.summarize_connection()

if __name__ == "__main__":
    main()
