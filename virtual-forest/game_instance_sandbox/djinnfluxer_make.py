import re
import ast
import json
import datetime

# Define the paths
file_path = 'sim.py'
output_path = 'dna_she.json'

class RNA_DNA_Mapper:
    def __init__(self):
        self.mapping = {
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

    def map_body(self, body):
        for construct, shorthand in self.mapping.items():
            replaced_body = re.sub(r'\b' + re.escape(construct) + r'\b', shorthand, body)
            if replaced_body != body:
                print(f"Replaced: {construct} -> {shorthand}")
            body = replaced_body
        return body

class CodeParser:
    def __init__(self, file_path, output_path, rna_dna_mapper):
        self.file_path = file_path
        self.output_path = output_path
        self.rna_dna_mapper = rna_dna_mapper

    def read_and_clean_file(self):
        cleaned_code_lines = []
        in_block_comment = False
        with open(self.file_path, 'r') as file:
            for line in file:
                # Handle block comments
                if '"""' in line or "'''" in line:
                    in_block_comment = not in_block_comment
                    continue
                if in_block_comment:
                    continue
                # Remove inline comments but preserve line
                cleaned_line = re.sub(r'#.*$', '', line)
                cleaned_code_lines.append(cleaned_line)
        return ''.join(cleaned_code_lines)

    def capture_raw_code(self, node, code_lines):
        start_line = node.lineno - 1
        end_line = node.end_lineno
        return "\n".join(code_lines[start_line:end_line]).strip()

    def parse_code_to_string(self, file_path):
        with open(file_path, 'r') as file:
            code_string = file.read()
        return code_string

    def create_code_entry(self):
        code_string = self.read_and_clean_file()
        if self.rna_dna_mapper:
            code_string = self.rna_dna_mapper.map_body(code_string)
        code_entry = {'code': code_string} # You can use any key you prefer instead of 'code'
        return code_entry

    def write_code_entry_to_json(self, code_entry):
        with open(self.output_path, 'w') as file:
            json.dump(code_entry, file, indent=4)

# Initialize the RNA_DNA_Mapper and CodeParser
rna_dna_mapper = RNA_DNA_Mapper()
parser = CodeParser(file_path, output_path, rna_dna_mapper)

# Define the metadata for the second DNA strand
current_timestamp = datetime.datetime.now().isoformat()
second_strand_metadata = {
    'metadata': {
        'version': '2.0',
        'author': 'AI',
        'description': 'Second DNA strand with metadata and versioning',
        'timestamp': current_timestamp
    }
}

# Create the second DNA strand entry with code and metadata
second_code_entry = parser.create_code_entry()
second_code_entry.update(second_strand_metadata)

# Load the existing JSON data (if it exists)
existing_json_data = {}
try:
    with open(output_path, 'r') as json_file:
        existing_json_data = json.load(json_file)
except FileNotFoundError:
    pass

existing_json_data['initial_strand'] = parser.create_code_entry()

# Use a different label for the second DNA strand
existing_json_data['second_strand'] = second_code_entry

# Write the updated JSON data back to the file
with open(output_path, 'w') as json_file:
    json.dump(existing_json_data, json_file, indent=4)