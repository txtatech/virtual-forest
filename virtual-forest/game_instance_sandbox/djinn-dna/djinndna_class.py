import re
import ast
import json

class CodeParser:
    def __init__(self, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path

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

    def parse_node(self, node, code_lines):
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
                'methods': [self.parse_node(method, code_lines) for method in node.body if isinstance(method, ast.FunctionDef)],
                'body': "\n".join(code_lines[node.lineno:node.end_lineno]).strip()
            }
        else:
            # Capture other constructs as raw code
            return self.capture_raw_code(node, code_lines)

    def parse_code_structure(self, code):
        code_lines = code.split("\n")
        parsed_ast = ast.parse(code)
        return [self.parse_node(node, code_lines) for node in ast.iter_child_nodes(parsed_ast) if self.parse_node(node, code_lines) is not None]

    def write_to_json_file(self, structure):
        with open(self.output_path, 'w') as file:
            json.dump(structure, file, indent=4)

    def parse_and_write_structure(self):
        cleaned_code = self.read_and_clean_file()
        rna_dna_structure_parsed_all = self.parse_code_structure(cleaned_code)
        self.write_to_json_file(rna_dna_structure_parsed_all)

if __name__ == "__main__":
    file_path = 'sim.py'  # Path to sim.py
    rna_dna_structure_path = 'rna_dna_structure.json'  # Output JSON file path

    parser = CodeParser(file_path, rna_dna_structure_path)
    parser.parse_and_write_structure()
