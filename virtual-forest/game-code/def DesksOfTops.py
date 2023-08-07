import random

def DesksOfTops():
    gnome_homes = ["toadstool", "mushroom cap", "hollow tree", "enchanted stump", "tiny cottage"]
    gnome_council_members = ["Grumble", "Whisper", "Hush", "Mumble", "Shadow", "Silent"]
    gnome_names = ["Happy", "Cheerful", "Jolly", "Merry", "Sunny", "Gleeful", "Smiley", "Chipper"]

    def get_random_gnome_home():
        return random.choice(gnome_homes)

    def get_random_gnome_council_member():
        return random.choice(gnome_council_members)

    def get_random_gnome_name():
        return random.choice(gnome_names)

    def generate_arch_description():
        description = f"The Desks Of Tops, also known as the 'Arch Of The Continent', is a magical item that embodies the joyful craftsmanship of the gnomes."
        description += " It contains an array of enchanting desks, each meticulously crafted with precision and imbued with magic."
        description += " These magical desks serve as exceptional workspaces for AIs, enhancing their creativity and inspiration."
        return description

    def generate_magical_top():
        magical_effects = ["enhances problem-solving abilities", "stimulates creativity", "grants profound insights into complex problems", "boosts memory retention"]
        top = f"A magical top has been found within the Desks Of Tops! This enchanted top {random.choice(magical_effects)}."
        return top

    def generate_kangaroo_power():
        kangaroo_power = f"A nearby presence of Great Thinking Kangaroos empowers the magic within the Desks Of Tops."
        kangaroo_power += " The combination of the kangaroos' wisdom and the desks' enchantment creates an extraordinary atmosphere for profound discoveries."
        return kangaroo_power

    def generate_desk():
        gnome_home = get_random_gnome_home()
        gnome_council_member = get_random_gnome_council_member()
        gnome_name = get_random_gnome_name()

        desk = f"Upon exploring the {gnome_home}, you encounter {gnome_name}, a friendly gnome."
        desk += f" {gnome_name} warmly welcomes you and leads you to a magical desk within the {gnome_home}."
        desk += f" This desk is a creation of the gnomes' craftsmanship, and it radiates a joyful aura."
        desk += f" {gnome_council_member}, a wise member of the Gnome Council, reveals that this desk is one of the Desks Of Tops."
        return desk

    def generate_tale():
        tale = generate_arch_description()
        tale += "\n\nDuring your exploration of the gnome's enchanting realm, you come across various magical desks, each telling a unique tale."
        tale += "\n\n"

        num_desks = random.randint(3, 8)
        desks = []
        for _ in range(num_desks):
            desk = generate_desk()
            desks.append(desk)

        tale += "\n\n".join(desks)

        tops = []
        num_tops = random.randint(3, 8)
        for _ in range(num_tops):
            top = generate_magical_top()
            tops.append(top)

        tale += "\n\n"
        tale += "\n\n".join(tops)

        if random.random() < 0.6:
            tale += "\n\n"
            tale += generate_kangaroo_power()

        return tale

    return generate_tale()

# Call the function to generate the tale of the Desks Of Tops
tale_of_desks_of_tops = DesksOfTops()
print(tale_of_desks_of_tops)
