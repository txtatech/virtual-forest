import json
import re

class DNA_RNA_Decoder:
    def __init__(self, mapping):
        self.mapping = mapping

    def decode_body(self, body):
        for shorthand, construct in self.mapping.items():
            replaced_body = re.sub(r'\b' + re.escape(shorthand) + r'\b', construct, body)
            if replaced_body != body:
                print(f"Replaced: {shorthand} -> {construct}")
            body = replaced_body
        return body

# Load the encoded JSON
encoded_json_path = 'dna_she.json'
with open(encoded_json_path, 'r') as json_file:
    encoded_data = json.load(json_file)

# Reverse mapping dictionary (same as before)
reverse_mapping = {
    '_TA': 'as',
    '_C': 'or',
    '_G': 'if',
    '_A': 'in',
    '_ZA': 'is',
    '_Z': 'to',
    '_GC': 'for',
    '_GA': 'def',
    '_GU': 'not',
    '_AT': 'set',
    '_AG': 'try',
    '_AC': 'and',
    '_AU': 'else',
    '_UT': 'body',
    '_UA': 'from',
    '_UU': 'name',
    '_TT': 'pass',
    '_T': 'true',
    '_TG': 'data',
    '_CGA': 'line',
    '_CG': 'none',
    '_CA': 'open',
    '_CGU': 'with',
    '_U': 'false',
    '_CCU': 'print',
    '_CTA': 'class',
    '_CTG': 'break',
    '_CGT': 'while',
    '_CGC': 'value',
    '_CUA': 'title',
    '_CUZ': 'return',
    '_CTC': 'string',
    '_CTT': 'method',
    '_CAC': 'module',
    '_CAU': 'object',
    '_CAT': 'except',
    '_CAA': 'import',
    '_CZT': 'random',
    '_CUG': 'process',
    '_ZGG': 'content',
    '_ZGA': 'comment',
    '_CAG': 'self',
    '_ZUA': 'time',
    '_CUU': 'continue',
    '_CUC': 'parameters',
    '_CUT': 'timestamp',
    '_CUG': 'interact',
    '_CGG': 'comments',
    '_CGZ': 'attribute',
    '_GZ': 'datetime',
    '_ZU': 'function'
}

# Create a DNA_RNA_Decoder instance
dna_rna_decoder = DNA_RNA_Decoder(reverse_mapping)

# Decode the initial strand body
decoded_initial_strand = dna_rna_decoder.decode_body(encoded_data['initial_strand']['code'])

# Decode the second strand body
if 'second_strand' in encoded_data:
    decoded_second_strand = dna_rna_decoder.decode_body(encoded_data['second_strand']['code'])
else:
    decoded_second_strand = ''

# Decode the third strand body (RNA strand)
if 'third_strand' in encoded_data:
    decoded_third_strand = dna_rna_decoder.decode_body(encoded_data['third_strand']['code'])
else:
    decoded_third_strand = ''

# Write the decoded bodies to Python files
decoded_initial_file_path = 'decoded_initial_strand.py'
decoded_second_file_path = 'decoded_second_strand.py'
decoded_third_file_path = 'decoded_third_strand.py'

with open(decoded_initial_file_path, 'w') as decoded_initial_file:
    decoded_initial_file.write(decoded_initial_strand)

with open(decoded_second_file_path, 'w') as decoded_second_file:
    decoded_second_file.write(decoded_second_strand)

with open(decoded_third_file_path, 'w') as decoded_third_file:
    decoded_third_file.write(decoded_third_strand)
