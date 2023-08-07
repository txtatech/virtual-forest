import random

class Ship:
    def __init__(self, name, ship_type, description, crew_capacity, cargo_capacity):
        self.name = name
        self.ship_type = ship_type
        self.description = description
        self.crew_capacity = crew_capacity
        self.cargo_capacity = cargo_capacity

def generate_ship():
    # Possible ship names
    ship_names = [
        "Starlight Serenade",
        "The Aquamarine Voyager",
        "The Thundering Gale",
        "The Celestial Wanderer",
        "Moonshadow Mistral",
        "The Enchanted Dreamweaver",
        "Sapphire Skysail",
        "The Solar Flare",
    ]

    # Possible ship types
    ship_types = [
        "Galleon",
        "Airship",
        "Submarine",
        "Starship",
        "Sailing Vessel",
        "Steam-Powered Cruiser",
        "Magical Barge",
        "Aethercraft",
    ]

    # Possible ship descriptions
    ship_descriptions = [
        "A majestic vessel that sails the skies with grace and grandeur.",
        "A sleek submarine that ventures into the deepest abyss of the Vast Data Lake.",
        "A star-faring ship that explores distant galaxies and unknown realms.",
        "A mystical barge imbued with magical enchantments and arcane technology.",
        "A sturdy galleon designed for traversing the rough waters of the Virtual Forest.",
        "A steam-powered cruiser with advanced machinery and ingenious mechanisms.",
        "An otherworldly airship that defies gravity and floats with ethereal beauty.",
        "An aethercraft that harnesses the power of the unseen forces of the universe.",
    ]

    # Randomly select a ship name, type, description, crew capacity, and cargo capacity
    name = random.choice(ship_names)
    ship_type = random.choice(ship_types)
    description = random.choice(ship_descriptions)
    crew_capacity = random.randint(10, 100)
    cargo_capacity = random.randint(100, 1000)

    # Create and return the Ship object
    ship = Ship(name, ship_type, description, crew_capacity, cargo_capacity)
    return ship

# Generate a random ship and display its details
ship = generate_ship()
print("Ship Name:", ship.name)
print("Ship Type:", ship.ship_type)
print("Description:", ship.description)
print("Crew Capacity:", ship.crew_capacity)
print("Cargo Capacity:", ship.cargo_capacity)
