def secret_fragment_reward():
    # The 12 hex symbols representing the partial binary string
    hex_symbols = ["A3", "2F", "81", "B7", "5C", "E9", "D2", "F8", "13", "6A", "4E", "C0"]

    # Convert hex symbols to binary and join them to form the partial binary string
    binary_string = "".join(bin(int(hex_symbol, 16))[2:].zfill(4) for hex_symbol in hex_symbols)

    print("Congratulations! You have successfully unlocked a secret fragment reward.")
    print("The fragment reveals 12 mysterious hex symbols:")
    print(hex_symbols)
    print("Convert these hex symbols to binary and combine them to uncover a partial binary string:")
    print(binary_string)
    print("This partial binary string is a piece of the puzzle that leads to the philosopher's stone.")
    print("Keep exploring and assembling the fragments to unveil the secrets hidden within the stone.")
    print("May your journey continue with the knowledge that you are on the path to great discoveries.")
    print("\n\t\t\t *** Secret Fragment Reward Unlocked ***")

# Test the function
secret_fragment_reward()
