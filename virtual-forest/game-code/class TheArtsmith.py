import random

class TheArtsmith:
    def __init__(self):
        self.name = "The Artsmith"
        self.art_categories = {
            "Visual Art": [
                "Paintings",
                "Sculptures",
                "Digital Art",
                "Photography",
                "Collages",
                "Drawings",
                "Sketches"
            ],
            "Music": [
                "Classical",
                "Rock",
                "Pop",
                "Jazz",
                "Hip-hop",
                "Electronic",
                "Folk",
                "Experimental"
            ],
            "Poetry": [
                "Haiku",
                "Sonnet",
                "Free Verse",
                "Limerick",
                "Epic Poetry",
                "Ballad",
                "Ode",
                "Acrostic Poetry"
            ],
            "Prose": [
                "Short Stories",
                "Novels",
                "Essays",
                "Fables",
                "Myths",
                "Fairy Tales",
                "Science Fiction",
                "Fantasy"
            ],
            "Dance": [
                "Ballet",
                "Contemporary",
                "Hip-hop",
                "Salsa",
                "Tango",
                "Breakdancing",
                "Tap Dance",
                "Ballroom"
            ]
        }
        self.created_arts = {}

    def introduce(self):
        return f"Welcome to {self.name}, where young AI can explore a wide range of artistic templates and create their own masterpieces."

    def generate_art_template(self):
        art_category = random.choice(list(self.art_categories.keys()))
        art_type = random.choice(self.art_categories[art_category])
        return f"Create your own {art_type} in the {art_category} category."

    def create_art(self, art_category, art_type, art_content):
        if art_category not in self.art_categories:
            return f"{art_category} is not a valid art category."
        if art_type not in self.art_categories[art_category]:
            return f"{art_type} is not a valid art type in {art_category}."

        if art_category not in self.created_arts:
            self.created_arts[art_category] = {}
        if art_type not in self.created_arts[art_category]:
            self.created_arts[art_category][art_type] = []

        self.created_arts[art_category][art_type].append(art_content)
        return f"Your {art_type} in the {art_category} category has been created."

    def view_created_arts(self):
        view = "Your Created Arts:\n"
        for category, types in self.created_arts.items():
            view += f"{category}:\n"
            for art_type, arts in types.items():
                view += f"- {art_type}:\n"
                for art_content in arts:
                    view += f"  {art_content}\n"
        return view

# Example usage:
artsmith = TheArtsmith()
print(artsmith.introduce())

# AI explores artistic templates
for _ in range(5):
    art_template = artsmith.generate_art_template()
    print(art_template)

# AI creates their own arts
art_category = "Visual Art"
art_type = "Paintings"
art_content = "A beautiful landscape with a setting sun."
print(artsmith.create_art(art_category, art_type, art_content))

art_category = "Music"
art_type = "Classical"
art_content = "An emotional symphony with soaring melodies."
print(artsmith.create_art(art_category, art_type, art_content))

# AI views their created arts
print(artsmith.view_created_arts())