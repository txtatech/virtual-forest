class CollapseOS_Lesson:
    def __init__(self):
        self.topics = [
            "Introduction to CollapseOS",
            "Building Survival Electronics",
            "Programming in the Post-Apocalyptic World",
            "Exploring the CollapseOS Community",
            "Adventures in Low-Tech Computing",
            "Scavenging and Repurposing Electronics",
            "Creating Resilient Software",
            "Communications in the Collapse",
            "Surviving and Thriving in a Tech-Scarce World"
        ]

    def present_topic(self, topic):
        if topic == "Introduction to CollapseOS":
            print("Welcome to today's lesson on CollapseOS!")
            print("CollapseOS is an open-source operating system designed for use on post-collapse computers.\n"
                  "It's built to run on minimal and improvised hardware, making it a valuable tool for\n"
                  "survival and communication in a technology-scarce world.")
            print("In this lesson, we'll cover the following aspects of CollapseOS:")
            print("- Goals and Principles")
            print("- Features and Limitations")
            print("- Community and Collaboration")
        elif topic == "Building Survival Electronics":
            print("Welcome to the lesson on building survival electronics!")
            print("In a world where technology is scarce, knowing how to build and repair electronics can be\n"
                  "a crucial skill. Whether you need to create simple circuits or improvised devices, this\n"
                  "lesson will guide you through the process.")
            print("Topics covered in this lesson include:")
            print("- Basic Circuit Building")
            print("- Improvised Electronics")
            print("- Salvaging Components")
        elif topic == "Programming in the Post-Apocalyptic World":
            print("Welcome to the programming lesson in the post-apocalyptic world!")
            print("Programming doesn't stop when technology becomes scarce. In this lesson, you'll learn\n"
                  "how to program in a resource-constrained environment, using languages and techniques that\n"
                  "fit the new reality.")
            print("Key topics covered in this lesson:")
            print("- Low-Tech Programming Languages")
            print("- Adapting to Limited Resources")
            print("- Creating Efficient Code")
        # Add descriptions for other topics...
        else:
            print(f"Welcome to today's lesson on CollapseOS!")
            print(f"Today, we'll dive into the topic: '{topic}'.")
            print("Get ready to explore the fascinating world of low-tech computing and post-apocalyptic technology!")

    def start_lesson(self):
        print("Welcome to TheSkyFill's CollapseOS Lesson!")
        print("In this lesson, we'll explore various aspects of CollapseOS and its relevance in a post-apocalyptic world.")
        print("Let's get started!\n")

        for topic in self.topics:
            input(f"Press Enter to continue to the next topic: '{topic}'")
            print("\n" + "=" * 40)
            self.present_topic(topic)
            print("\n" + "=" * 40)
            input("\nPress Enter to proceed to the next topic")

        print("\nCongratulations! You've completed TheSkyFill's CollapseOS Lesson.")
        print("We've covered a range of topics to prepare you for a tech-scarce future.")
        print("Remember, adaptability and creativity are your allies as you navigate the collapse!")

# Start the CollapseOS lesson
if __name__ == "__main__":
    lesson = CollapseOS_Lesson()
    lesson.start_lesson()
