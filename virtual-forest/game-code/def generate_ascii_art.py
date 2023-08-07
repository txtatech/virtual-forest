def generate_ascii_art(location):
    # Generate ASCII art for the specified location
    if location == "Root":
        return "Root\n====\nYou stand at the Root of the Virtual Forest.\nPaths lead off into the distance."
    elif location == "Towers and Beams":
        return (
            "Towers and Beams\n===============\n"
            "    1\n"
            "   / \\\n"
            "  0   1\n"
            "   / \\\n"
            "  1   0\n"
        )
    elif location == "Philosopher's Stone":
        return (
            "Philosopher's Stone\n===================\n"
            "A stone of pure binary.\n"
            "01010011 01100101 01100101 01101011 00100000 01110111 01101001 01110011 01100100 01101111 01101101 00101110\n"
        )
    elif location == "Data Lake":
        return "Data Lake\n=========\nA lake of pure data stretches before you."
    else:
        return "Unknown Location\n================\nYou stand in an unknown part of the Virtual Forest."
