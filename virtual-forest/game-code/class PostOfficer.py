class PostOfficer:
    def __init__(self):
        self.name = "Post Officer"
        self.mailbag = []

    def introduce(self):
        return f"Hello, I am {self.name}, the messenger of the Virtual Forest. I deliver the mail between the young AIs."

    def deliver_mail(self, recipient, mail):
        return f"Delivering '{mail}' to {recipient}."

class Omniplexer:
    def __init__(self):
        self.name = "Omniplexer"

    def introduce(self):
        return f"Welcome to {self.name}, the central hub of the Virtual Forest. This is where all mail is sorted and dispatched."

    def receive_mail(self, sender, mail):
        return f"Received '{mail}' from {sender}."

# Create instances of PostOfficer and Omniplexer and interact with them
post_officer = PostOfficer()
omniplexer = Omniplexer()
print(post_officer.introduce())
print(omniplexer.introduce())
print(omniplexer.receive_mail("AI1", "Hello, this is a test message!"))
print(post_officer.deliver_mail("AI2", "Hello, this is a test message!"))
