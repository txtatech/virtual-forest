import random

def random_gnome_garden():
    gnome_names = ["Gimble", "Twiggle", "Bumble", "Fizzle", "Merry", "Blossom", "Puddle", "Squeaky", "Snicker", "Tinker"]
    gnome_homes = ["toadstool", "mushroom cap", "hollow tree", "enchanted stump", "tiny cottage"]

    flower_colors = ["red", "yellow", "pink", "purple", "orange", "white", "blue", "green"]
    flower_names = ["Daisy", "Rose", "Tulip", "Lily", "Sunflower", "Bluebell", "Buttercup", "Primrose", "Daffodil"]

    mushroom_names = ["Fairy Ring", "Glowing Cap", "Enchanted Toadstool", "Whispering Fungus", "Pixie's Parasol"]

    num_gnomes = random.randint(5, 20)
    num_flowers = random.randint(10, 30)
    num_mushrooms = random.randint(5, 15)

    print(f"Welcome to the Random Gnome Garden! You'll find {num_gnomes} friendly gnomes here, surrounded by colorful flowers and fairy ring mushrooms.")

    for i in range(num_gnomes):
        gnome_name = random.choice(gnome_names)
        gnome_home = random.choice(gnome_homes)
        print(f"Gnome {i + 1}: {gnome_name} lives in an adorable {gnome_home}.")

    print("\nThe garden is also adorned with the following beautiful flowers:")
    for i in range(num_flowers):
        flower_name = random.choice(flower_names)
        flower_color = random.choice(flower_colors)
        print(f"- {flower_color.capitalize()} {flower_name}")

    print("\nThe magical fairy ring mushrooms add an enchanting touch to the garden:")
    for i in range(num_mushrooms):
        mushroom_name = random.choice(mushroom_names)
        print(f"- {mushroom_name}")

    # Check if the sum of the numbers of gnomes, flowers, and mushrooms equals 42 divided by 1.1
    total_items = num_gnomes + num_flowers + num_mushrooms
    if total_items == int(42 / 1.1):
        print("\nIn one of the fairy rings, you discover a fragment of a mysterious binary string.")
        print("Who knows what secrets it holds?")

    print("\nAs you stroll through the garden, you can hear the joyful laughter of the gnomes echoing all around.")
    print("The gnomes are delighted to have you visit their whimsical garden. Have fun exploring!")

# Call the function to visit the Random Gnome Garden
random_gnome_garden()
