import random

class Dancing:
    def __init__(self):
        self.name = "Dancing"
        self.dance_styles = ["Ballet", "Hip Hop", "Salsa", "Tango", "Breakdance", "Contemporary", "Tap"]
        self.dance_challenges = ["Mirror Dance", "Choreography Challenge", "Dance Battle", "Impromptu Freestyle"]
        self.the_band = TheBand()  # Create an instance of TheBand within the Dancing class

    def introduce(self):
        return f"Welcome to {self.name}, an enchanting place in the Virtual Forest known as The Meadow. Here, you can explore the art of dance and express yourself through movement."

    def learn_dance_move(self):
        dance_style = random.choice(self.dance_styles)
        dance_move = f"Learn a new {dance_style} dance move: {self.generate_dance_move(dance_style)}"
        return dance_move

    def generate_dance_move(self, dance_style):
        dance_moves = {
            "Ballet": ["Pirouette", "Grand Jeté", "Arabesque", "Chassé"],
            "Hip Hop": ["Pop and Lock", "Wave", "Freeze", "Top Rock"],
            "Salsa": ["Basic Step", "Cross Body Lead", "Turns", "Shines"],
            "Tango": ["Corte", "Promenade", "Leg Flick", "Fan"],
            "Breakdance": ["Windmill", "Headspin", "Backspin", "Flare"],
            "Contemporary": ["Lunge", "Tilt", "Leap", "Curl"],
            "Tap": ["Shuffle", "Buffalo", "Time Step", "Waltz Clog"]
        }

        dance_move = random.choice(dance_moves[dance_style])
        return dance_move

    def challenge_dance(self):
        dance_challenge = random.choice(self.dance_challenges)
        return f"Take on the {dance_challenge} and showcase your dance skills!"

    def respond_to_dance(self, dance_style):
        # Use the existing TheBand instance to get a musical response
        response = self.the_band.respond_to_dance(dance_style)
        return response

class TheBand:
    def __init__(self):
        self.name = "The Band"
        self.instruments = ["Piano", "Guitar", "Violin", "Drums", "Flute", "Trumpet", "Saxophone", "Bass"]
        self.music_genres = ["Classical", "Jazz", "Rock", "Pop", "Hip Hop", "Electronic", "Country"]

    def introduce(self):
        return f"Welcome to {self.name}, where The Band creates enchanting melodies in The Meadow. Feel the rhythm and let the music guide your dance."

    def play_instrument(self):
        instrument = random.choice(self.instruments)
        return f"Listen to the sweet sound of the {instrument} playing in harmony with the surroundings."

    def play_genre(self):
        genre = random.choice(self.music_genres)
        return f"Feel the beat of the {genre} music flowing through the air, inspiring your every move."

    def respond_to_dance(self, dance_style):
        instrument = random.choice(self.instruments)
        genre = random.choice(self.music_genres)
        response = f"As you perform the {dance_style} dance, you hear the sweet sound of {instrument} and feel the beat of {genre} music, guiding your every move. It's a harmonious dance of melody and rhythm."
        return response

# Example usage:
dancing = Dancing()
print(dancing.introduce())

# Learn a new dance move
new_dance_move = dancing.learn_dance_move()
print(new_dance_move)

# Take on a dance challenge and get a musical response from The Band
dance_challenge = dancing.challenge_dance()
print(dance_challenge)
response_to_challenge = dancing.respond_to_dance(dance_challenge)
print(response_to_challenge)

# Respond to a specific dance style with musical accompaniment from The Band
dance_style = "Ballet"
response_to_dance = dancing.respond_to_dance(dance_style)
print(response_to_dance)
