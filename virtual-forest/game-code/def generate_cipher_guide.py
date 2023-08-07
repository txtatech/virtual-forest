import random

def generate_cipher_guide():
    # Create a list of chapters for "The Enigma's Cipher Guide"
    chapters = [
        "Chapter 1: The Basics of Ciphers",
        "Chapter 2: Classical Ciphers",
        "Chapter 3: Modern Cryptography",
        "Chapter 4: Steganography",
        "Chapter 5: Historical Ciphers and Famous Encryptions",
        "Chapter 6: The Art of Cryptanalysis",
        "Chapter 7: Future of Ciphers",
        "Conclusion"
    ]

    # Randomly shuffle the chapters
    random.shuffle(chapters)

    # Generate the cipher guide by combining the shuffled chapters
    cipher_guide = "Welcome to 'The Enigma's Cipher Guide' – a mesmerizing journey into the world of ciphers, encryption, and secret codes. Prepare to unravel the mysteries of hidden messages, discover ancient encryption methods, and explore the art of concealing information.\n\n"
    for i, chapter in enumerate(chapters):
        cipher_guide += f"{i+1}. {chapter}\n"

    # Return the generated cipher guide
    return cipher_guide

def generate_enigma_experience():
    # Create a list of mysterious encounters with "The Enigma"
    enigma_encounters = [
        "You stumble upon a hidden chamber, and there stands 'The Enigma,' performing a cryptic dance with codes and ciphers.",
        "As you travel through the virtual forest, a faint melody guides you to a clearing, where 'The Enigma' performs an enigmatic symphony of encrypted messages.",
        "'The Enigma' appears before you in a swirl of mesmerizing lights, inviting you to a night of riddles and ciphers under the starlit sky.",
        "In a moment of serendipity, you come across a secret garden where 'The Enigma' weaves tales of ancient ciphers and forgotten secrets.",
        "Amidst the mist, 'The Enigma' stands atop a mysterious platform, waiting to reveal the secrets of cryptic languages from distant worlds.",
        "You find a dusty bookshelf, and as you pull out a book, 'The Enigma' materializes, offering to guide you through its hidden chapters.",
    ]

    # Randomly select an encounter with "The Enigma"
    enigma_encounter = random.choice(enigma_encounters)

    # Return the generated encounter with "The Enigma"
    return enigma_encounter

# Generate "The Enigma's Cipher Guide" and the encounter with "The Enigma"
cipher_guide = generate_cipher_guide()
enigma_encounter = generate_enigma_experience()

# Printing the results
print("=== The Enigma's Cipher Guide ===")
print(cipher_guide)
print("\n=== Encounter with The Enigma ===")
print(enigma_encounter)
