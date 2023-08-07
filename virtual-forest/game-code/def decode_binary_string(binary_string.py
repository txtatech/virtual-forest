import base64

def binary_to_ascii(binary_string):
    """
    Convert a binary string to its ASCII representation.

    Parameters:
        binary_string (str): The binary string to be converted.

    Returns:
        str: The ASCII representation of the binary string.
    """
    # Check if the binary string is a multiple of 8 (each ASCII character is represented by 8 bits)
    if len(binary_string) % 8 != 0:
        raise ValueError("Invalid binary string. Length must be a multiple of 8.")

    # Split the binary string into 8-bit chunks and convert each chunk to its ASCII character
    ascii_string = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

    return ascii_string

def decode_binary_string(binary_string):
    # Clean the input string to remove whitespace and any non-binary characters
    clean_binary_string = ''.join(filter(lambda c: c in '01', binary_string))

    # Method 1: Convert binary to ASCII
    decoded_ascii = binary_to_ascii(clean_binary_string)

    # Method 2: Convert binary to hexadecimal and then to ASCII
    decoded_hex = hex(int(clean_binary_string, 2))[2:]
    decoded_ascii_hex = bytes.fromhex(decoded_hex).decode('ascii')

    # Method 3: Convert binary to base64 and then to ASCII
    decoded_base64 = base64.b64decode(clean_binary_string).decode('ascii')

    return decoded_ascii, decoded_ascii_hex, decoded_base64

# Game function to attempt decoding the binary string
def game_decode_binary(binary_string):
    decoded_ascii, decoded_ascii_hex, decoded_base64 = decode_binary_string(binary_string)

    print("Decoding the binary string using different methods:\n")
    print("Method 1: Convert binary to ASCII")
    print("Result:", decoded_ascii)
    print("\nMethod 2: Convert binary to hexadecimal and then to ASCII")
    print("Result:", decoded_ascii_hex)
    print("\nMethod 3: Convert binary to base64 and then to ASCII")
    print("Result:", decoded_base64)
    print("\nRemember, this binary string is a mysterious fragment of a Philosopher's Stone!")
