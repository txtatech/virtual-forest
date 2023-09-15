from djinnfluxer import DjinnFluxer
from djinnfluxer_she_make import DNA_RNA_Decoder
from djinnfluxer_make import RNA_DNA_Mapper
import json

# Path to the JSON file containing the DNA data
json_path = 'dna_she.json'

# Mapping dictionary (defined in djinnfluxerX.py)
mapping = {
    'as': '_TA',
    'or': '_C',
    'if': '_G',
    'in': '_A',
    'is': '_ZA',
    'to': '_Z',
    'for': '_GC',
    'def': '_GA',
    'not': '_GU',
    'set': '_AT',
    'try': '_AG',
    'and': '_AC',
    'else': '_AU',
    'body': '_UT',
    'from': '_UA',
    'name': '_UU',
    'pass': '_TT',
    'true': '_T',
    'data': '_TG',
    'line': '_CGA',
    'none': '_CG',
    'open': '_CA',
    'with': '_CGU',
    'false': '_U',
    'print': '_CCU',
    'class': '_CTA',
    'break': '_CTG',
    'while': '_CGT',
    'value': '_CGC',
    'title': '_CUA',
    'return': '_CUZ',
    'string': '_CTC',
    'method': '_CTT',
    'module': '_CAC',
    'object': '_CAU',
    'except': '_CAT',
    'import': '_CAA',
    'random': '_CZT',
    'process': '_CUG',
    'content': '_ZGG',
    'comment': '_ZGA',
    'self': '_CAG',
    'time': '_ZUA',
    'continue': '_CUU',
    'parameters': '_CUC',
    'timestamp': '_CUT',
    'interact': '_CUG',
    'comments': '_CGG',
    'attribute': '_CGZ',
    'datetime': '_GZ',
    'function': '_ZU'
}

# Create DjinnFluxer instance
djinn_fluxer = DjinnFluxer(json_path, mapping)

# Interact with DNA
djinn_fluxer.interact_with_dna()

# Load the encoded JSON
with open(json_path, 'r') as json_file:
    encoded_data = json.load(json_file)

# Reverse mapping dictionary (defined in dna_rna_decoder.py)
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

# Decode the strands and write to files
# ...

print("DNA and RNA interaction complete.")
