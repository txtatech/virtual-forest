import re

# Generating all possible combinations of 'T', 'A', 'C', and 'G', ranging from one to four characters long
characters = ['T', 'A', 'C', 'G']
combinations = [f"_{char}" for char in characters]
for _ in range(3):  # Repeat three times to extend to four characters long
    combinations = [f"{combo}{char}" for combo in combinations for char in characters]

# Initializing a dictionary to store word counts
word_frequency_filtered = {}

# Reading the sim.py file and counting occurrences of non-empty words
with open('sim.py', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = re.sub(r'[^\w\s]', '', word).lower()  # Removing punctuation and converting to lowercase
            if word.strip():  # Excluding empty strings or whitespace
                word_frequency_filtered[word] = word_frequency_filtered.get(word, 0) + 1

# Filtering words that occur more than four times
words_more_than_four_times_filtered = {word: count for word, count in word_frequency_filtered.items() if count > 4}

# Initializing a dictionary to store the key-value pairs
key_value_mapping_filtered = {}

# Mapping non-empty words to the combinations
combination_index = 0
for word, count in words_more_than_four_times_filtered.items():
    if combination_index < len(combinations):
        key_value_mapping_filtered[word] = combinations[combination_index]
        combination_index += 1
    else:
        # If we run out of combinations, stop the mapping
        break

# Writing the filtered key-value pairs to the output.txt file
with open('output.txt', 'w') as file:
    file.write("{\n")
    for key, value in key_value_mapping_filtered.items():
        file.write(f"  '{key}':'{value}',\n")
    file.write("}\n")
