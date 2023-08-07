import random

def craft_gangway_planks():
    # Possible materials for crafting the Gangway Planks
    materials = [
        "Ancient Oak Wood",
        "Glowing Crystal",
        "Silver-Infused Steel",
        "Enchanted Sapphire",
        "Starlit Silk",
        "Iridescent Moonstone",
        "Celestial Feather",
        "Rainbow Glass",
    ]

    # Possible styles for the Gangway Planks
    styles = [
        "Elven Elegance",
        "Dwarven Durability",
        "Fey Enchantment",
        "Celestial Grace",
        "Mystic Runes",
        "Nature's Harmony",
        "Mechanical Marvel",
        "Ethereal Whispers",
    ]

    # Randomly select a material and style for the Gangway Planks
    selected_material = random.choice(materials)
    selected_style = random.choice(styles)

    # Randomly generate a length for the Gangway Planks
    length = random.randint(10, 50)

    # Randomly generate a color for the Gangway Planks
    colors = ["Crimson", "Azure", "Emerald", "Amethyst", "Golden", "Pearlescent", "Silver"]
    selected_color = random.choice(colors)

    # Assemble the Gangway Planks description
    description = f"A set of Gangway Planks crafted from {selected_material} in a {selected_style} style."
    description += f" The planks are {length} feet long and emanate a {selected_color} glow."

    return description

# Generate and display a set of Gangway Planks
gangway_planks = craft_gangway_planks()
print(gangway_planks)