import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def parse_json_structure(structure, indentation_level=0):
    code_lines = []
    for element in structure:
        if isinstance(element, dict):
            if element['type'] == 'function':
                code_lines.append("    " * indentation_level + f"def {element['name']}({', '.join(element['parameters'])}):")
                body_indentation = element['body'].replace('\\n', '\\n' + "    " * (indentation_level + 1))
                code_lines.append("    " * (indentation_level + 1) + f"{body_indentation}")
            elif element['type'] == 'class':
                code_lines.append("    " * indentation_level + f"class {element['name']}:")
                code_lines.extend(parse_json_structure(element['methods'], indentation_level + 1))
                body_indentation = element['body'].replace('\\n', '\\n' + "    " * (indentation_level + 1))
                code_lines.append("    " * (indentation_level + 1) + f"{body_indentation}")
        else:
            # Handle raw code lines and preserve blank lines
            code_lines.extend(["    " * indentation_level + line for line in element.split('\\n')])
    return code_lines

def write_to_python_file(code_lines, file_path):
    with open(file_path, 'w') as file:
        file.write('\n'.join(code_lines))

json_file_path = 'rna_dna_structure.json'  # Path to JSON file
python_file_path = 'sim_dna.py'  # Output Python file path

# Read the content of the JSON file
json_structure = read_json_file(json_file_path)

# Parse the JSON structure into Python code
parsed_code_lines = parse_json_structure(json_structure)

# Write the parsed code to the sim_dna.py file
write_to_python_file(parsed_code_lines, python_file_path)
