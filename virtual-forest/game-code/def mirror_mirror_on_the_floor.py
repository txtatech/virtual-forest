import random

def mirror_mirror_on_the_floor():
    atada_brothers = ["ATAD", "Lore"]
    selected_brother = random.choice(atada_brothers)

    if selected_brother == "ATAD":
        print("Mirror Mirror on the floor, who speaks louder, Data or Lore?")
        print("ATAD's reflection appears in the mirror and answers, 'Data.'")
        return "Data"
    elif selected_brother == "Lore":
        print("Mirror Mirror on the floor, who speaks louder, Data or Lore?")
        print("Lore's reflection appears in the mirror and answers, 'Lore.'")
        return "Lore"

# Example usage:
result = mirror_mirror_on_the_floor()
