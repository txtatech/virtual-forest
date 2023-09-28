import re

# Generating all possible combinations of 'T', 'A', 'C', and 'G', ranging from one to four characters long
characters = ['T', 'A', 'C', 'G']
combinations = [f"{char}" for char in characters]

# Initialize a list to store mappings
generated_mappings = []

# Generate mappings for single characters
generated_mappings.extend(combinations)

# Generate mappings for combinations of two characters
generated_mappings.extend([f"{char1}{char2}" for char1 in combinations for char2 in combinations])

# Generate mappings for combinations of three characters
generated_mappings.extend([f"{char1}{char2}{char3}" for char1 in combinations for char2 in combinations for char3 in combinations])

# Generate mappings for combinations of four characters
generated_mappings.extend([f"{char1}{char2}{char3}{char4}" for char1 in combinations for char2 in combinations for char3 in combinations for char4 in combinations])

# Initialize a dictionary to store word counts
word_frequency_filtered = {}

# Reading the sim.py file and counting occurrences of non-empty words
with open('sim.py', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = re.sub(r'[^\w\s]', '', word).lower()  # Removing punctuation and converting to lowercase
            if word.strip():  # Excluding empty strings or whitespace
                word_frequency_filtered[word] = word_frequency_filtered.get(word, 0) + 1

# Filtering words that occur four or more times
words_four_or_more_times_filtered = {word: count for word, count in word_frequency_filtered.items() if count >= 4}

# Writing the generated key-value pairs to the output.txt file
with open('output.txt', 'w') as file:
    file.write("{\n")
    for word, code in zip(words_four_or_more_times_filtered, generated_mappings):
        file.write(f"  '{word}':'_{code}',\n")
    file.write("}\n")

# Read the original mapping from 'output.txt' and reverse it
with open('output.txt', 'r') as file:
    mapping = eval(file.read())

# Create the reverse mapping
reverse_mapping = {v.strip("'_"): k for k, v in mapping.items()}

# Write the reversed mapping to 'reverse-mappings.txt'
with open('reverse-mappings.txt', 'w') as file:
    file.write("{\n")
    for code, word in reverse_mapping.items():
        file.write(f"  '{word}':'_{code}',\n")
    file.write("}\n")

