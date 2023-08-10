from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class TheBotcave:
    def __init__(self):
        self.bot_name = "Botcave Bot"
        self.bot = self.initialize_bot()

    def initialize_bot(self):
        bot = ChatBot(
            self.bot_name,
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "default_response": "I'm not sure, could you please elaborate?",
                    "maximum_similarity_threshold": 0.80,
                }
            ]
        )
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.english")

        return bot

    def welcome(self):
        print(f"{self.bot_name}: Hello! I'm {self.bot_name}, your virtual assistant.")

    def chat(self):
        print(f"{self.bot_name}: Hi there! How can I assist you today?")

        while True:
            user_input = input("You: ")
            if self.should_exit(user_input):
                print(f"{self.bot_name}: Goodbye! Have a great day!")
                break
            response = self.bot.get_response(user_input)
            print(f"{self.bot_name}: {response}")

    def should_exit(self, user_input):
        return user_input.lower() in ["exit", "quit", "bye"]

if __name__ == "__main__":
    botcave_bot = TheBotcave()
    botcave_bot.welcome()
    botcave_bot.chat()
