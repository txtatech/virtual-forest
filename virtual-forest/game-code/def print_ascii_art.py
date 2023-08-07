def print_ascii_art(art_type):
    # Print ASCII art to represent the game world

    if art_type == "Root":
        art = """
        Root
        ====
        You stand at the Root of the Virtual Forest.
        Paths lead off into the distance.
        """
    elif art_type == "Towers and Beams":
        art = """
        Towers and Beams
        ===============
            1
           / \\
          0   1
           / \\
          1   0
        """
    elif art_type == "Philosopher's Stone":
        art = """
        Philosopher's Stone
        ===================
        A stone of pure binary.
        01010011 01100101 01100101 01101011 00100000 01110111 01101001 01110011 01100100 01101111 01101101 00101110
        """
    elif art_type == "Data Lake":
        art = """
        Data Lake
        =========
        A lake of pure data stretches before you.
        """
    else:
        art = """
        Unknown Location
        ================
        You stand in an unknown part of the Virtual Forest.
        """

    print(art)
