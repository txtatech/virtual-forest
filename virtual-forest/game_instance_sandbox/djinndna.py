import re
import ast
import json

def read_and_clean_file(file_path):
    cleaned_code_lines = []
    in_block_comment = False
    with open(file_path, 'r') as file:
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

def capture_raw_code(node, code_lines):
    start_line = node.lineno - 1
    end_line = node.end_lineno
    return "\n".join(code_lines[start_line:end_line]).strip()

def parse_node(node, code_lines):
    if isinstance(node, ast.FunctionDef):
        return {
            'type': 'function',
            'name': node.name,
            'parameters': [param.arg for param in node.args.args],
            'body': "\n".join(code_lines[node.lineno:node.end_lineno]).strip()
        }
    elif isinstance(node, ast.ClassDef):
        return {
            'type': 'class',
            'name': node.name,
            'methods': [parse_node(method, code_lines) for method in node.body if isinstance(method, ast.FunctionDef)],
            'body': "\n".join(code_lines[node.lineno:node.end_lineno]).strip()
        }
    else:
        # Capture other constructs as raw code
        return capture_raw_code(node, code_lines)

def parse_code_structure(code):
    code_lines = code.split("\n")
    parsed_ast = ast.parse(code)
    return [parse_node(node, code_lines) for node in ast.iter_child_nodes(parsed_ast) if parse_node(node, code_lines) is not None]

def write_to_json_file(structure, file_path):
    with open(file_path, 'w') as file:
        json.dump(structure, file, indent=4)

file_path = 'sim.py'  # Path to sim.py
rna_dna_structure_path = 'rna_dna_structure.json'  # Output JSON file path

# Read and clean the content of sim.py
cleaned_code = read_and_clean_file(file_path)

# Parse the cleaned code into the DNA/RNA structure
rna_dna_structure_parsed_all = parse_code_structure(cleaned_code)

# Write the parsed RNA/DNA structure to the JSON file
write_to_json_file(rna_dna_structure_parsed_all, rna_dna_structure_path)
