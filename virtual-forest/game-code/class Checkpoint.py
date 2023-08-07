import random

class Checkpoint:
    def __init__(self, name, location, services):
        self.name = name
        self.location = location
        self.services = services

def generate_checkpoint():
    # Possible checkpoint names
    checkpoint_names = [
        "Riverside Haven",
        "Data Junction",
        "Dataflow Nexus",
        "Harbor Gate",
        "The Streamwatch",
        "Data Portico",
        "Wavefront Gateway",
    ]

    # Possible checkpoint locations
    checkpoint_locations = [
        "At the confluence of the Vast Data Lake and the River",
        "Nestled within the heart of the Virtual Forest",
        "Guarding the passage to the Ocean",
        "Where the river winds through the Flitting Woods",
        "Near the Code Cavern and the Watery Keep",
        "Where the Sub-Slanguage Express crosses the river",
        "By the mythical Waterfall of Wisdom",
    ]

    # Possible checkpoint services
    checkpoint_services = [
        "Inspecting passing ships for safety and compliance",
        "Assisting ships with navigation and route planning",
        "Providing rest and refueling stations for weary travelers",
        "Offering trade and exchange of data artifacts",
        "Conducting customs and data clearance procedures",
        "Monitoring and regulating data flow to prevent congestion",
        "Extending invitations to special events and gatherings",
    ]

    # Randomly select a checkpoint name, location, and services
    name = random.choice(checkpoint_names)
    location = random.choice(checkpoint_locations)
    services = random.sample(checkpoint_services, random.randint(2, 4))

    # Create and return the Checkpoint object
    checkpoint = Checkpoint(name, location, services)
    return checkpoint

# Generate three random checkpoints along the river and display their details
checkpoints = [generate_checkpoint() for _ in range(3)]
for i, checkpoint in enumerate(checkpoints, 1):
    print(f"Checkpoint {i}:")
    print("Name:", checkpoint.name)
    print("Location:", checkpoint.location)
    print("Services:", ', '.join(checkpoint.services))
    print()