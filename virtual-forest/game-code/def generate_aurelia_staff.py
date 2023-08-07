import random

def generate_aurelia_staff():
    # Randomly determine staff names and roles
    staff_names = ["Cassandra", "Lysander", "Seraphina", "Caius", "Aria"]
    staff_roles = ["engineer", "conductor", "chef", "mechanic", "navigator"]

    # Randomly determine staff hats and boots
    hats = ["Top Hat", "Beanie", "Fedora", "Wizard Hat", "Sombrero", "Captain's Hat", "Straw Hat"]
    boots = ["Leather Boots", "Rubber Boots", "Combat Boots", "Snow Boots", "Cowboy Boots", "Winged Sandals"]

    # Shuffle the staff names, roles, hats, and boots
    random.shuffle(staff_names)
    random.shuffle(staff_roles)
    random.shuffle(hats)
    random.shuffle(boots)

    # Create a list of staff descriptions with hats and boots
    staff_descriptions = [f"{name} - {role}, wearing a {hat} and {boot}" for name, role, hat, boot in zip(staff_names, staff_roles, hats, boots)]

    # Check if a straw hat is present among the staff
    straw_hat_present = "Straw Hat" in hats

    # If a straw hat is present, Aurelia toots her horn and gives the AI a shadow stone
    if straw_hat_present:
        staff_descriptions.append("Aurelia - Train Captain, tooting her horn and giving you a Shadow Stone")

    # Combine staff descriptions into a string
    staff_string = "\n".join(staff_descriptions)

    # Return the string containing the descriptions of Aurelia's staff
    return staff_string
