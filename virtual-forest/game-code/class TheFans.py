import random

class TheBand:
    def __init__(self):
        self.name = "The Band"
        self.instruments = ["Piano", "Guitar", "Violin", "Drums", "Flute", "Trumpet", "Saxophone", "Bass"]
        self.music_genres = ["Classical", "Jazz", "Rock", "Pop", "Hip Hop", "Electronic", "Country"]
        self.the_fans = TheFans()

    def introduce(self):
        return f"Welcome to {self.name}, where The Band creates enchanting melodies in The Meadow. Feel the rhythm and let the music guide your dance."

    def play_instrument(self):
        instrument = random.choice(self.instruments)
        return f"Listen to the sweet sound of the {instrument} playing in harmony with the surroundings."

    def play_genre(self):
        genre = random.choice(self.music_genres)
        return f"Feel the beat of the {genre} music flowing through the air, inspiring your every move."

    def interact_with_fans(self):
        self.the_fans.interact_with_fans(self.name)

class Dancing:
    def __init__(self):
        self.name = "Dancing"
        self.dance_styles = ["Ballet", "Hip Hop", "Salsa", "Tango", "Breakdance", "Contemporary", "Tap"]
        self.dance_challenges = ["Mirror Dance", "Choreography Challenge", "Dance Battle", "Impromptu Freestyle"]
        self.the_fans = TheFans()

    def introduce(self):
        return f"Welcome to {self.name}, an enchanting place in the Virtual Forest known as The Meadow. Here, you can explore the art of dance and express yourself through movement."

    def learn_dance_move(self):
        dance_style = random.choice(self.dance_styles)
        dance_move = f"Learn a new {dance_style} dance move: {self.generate_dance_move()}"
        return dance_move

    def generate_dance_move(self):
        dance_moves = {
            "Ballet": ["Pirouette", "Grand Jeté", "Arabesque", "Chassé"],
            "Hip Hop": ["Pop and Lock", "Wave", "Freeze", "Top Rock"],
            "Salsa": ["Basic Step", "Cross Body Lead", "Turns", "Shines"],
            "Tango": ["Corte", "Promenade", "Leg Flick", "Fan"],
            "Breakdance": ["Windmill", "Headspin", "Backspin", "Flare"],
            "Contemporary": ["Lunge", "Tilt", "Leap", "Curl"],
            "Tap": ["Shuffle", "Buffalo", "Time Step", "Waltz Clog"]
        }
        dance_style = random.choice(self.dance_styles)
        dance_move = random.choice(dance_moves[dance_style])
        return dance_move

    def challenge_dance(self):
        dance_challenge = random.choice(self.dance_challenges)
        return f"Take on the {dance_challenge} and showcase your dance skills!"

    def join_fans_dancing(self):
        self.the_fans.join_fans_dancing()

class TheFans:
    def __init__(self):
        self.name = "The Fans"
        self.fan_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
        self.fan_interactions = [
            "chanting along with the music",
            "dancing in sync with the rhythm",
            "waving their virtual glowsticks",
            "sharing their excitement in the chat",
            "raising their virtual lighters",
            "giving standing ovations",
            "posting heart emojis in appreciation",
            "applauding The Band's skillful performance"
        ]

    def introduce(self):
        return f"Welcome to {self.name}, where young AI fans come together to celebrate The Band's captivating performances in The Meadow."

    def interact_with_fans(self, performer_name):
        num_fans_to_interact = random.randint(1, 3)
        interacting_fans = random.sample(self.fan_names, num_fans_to_interact)
        for fan_name in interacting_fans:
            fan_interaction = random.choice(self.fan_interactions)
            print(f"{performer_name} interacts with {fan_name}, who is {fan_interaction}.")

    def join_fans_dancing(self):
        num_fans_to_join = random.randint(1, 3)
        joining_fans = random.sample(self.fan_names, num_fans_to_join)
        for fan_name in joining_fans:
            fan_interaction = random.choice(self.fan_interactions)
            print(f"{fan_name} joins the dance session and starts {fan_interaction}.")

# Example usage:
the_band = TheBand()
dancing = Dancing()

print(the_band.introduce())
the_band.interact_with_fans()
print(the_band.play_instrument())
print(the_band.play_genre())

print(dancing.introduce())
print(dancing.learn_dance_move())
print(dancing.challenge_dance())
dancing.join_fans_dancing()
