import json

class JsonToCodeConverter:
    def __init__(self, json_file_path, python_file_path):
        self.json_file_path = json_file_path
        self.python_file_path = python_file_path

    def read_json_file(self):
        with open(self.json_file_path, 'r') as file:
            return json.load(file)

    def parse_json_structure(self, structure, indentation_level=0):
        code_lines = []
        for element in structure:
            if isinstance(element, dict):
                if element['type'] == 'function':
                    code_lines.append("    " * indentation_level + f"def {element['name']}({', '.join(element['parameters'])}):")
                    body_indentation = element['body'].replace('\\n', '\\n' + "    " * (indentation_level + 1))
                    code_lines.append("    " * (indentation_level + 1) + f"{body_indentation}")
                elif element['type'] == 'class':
                    code_lines.append("    " * indentation_level + f"class {element['name']}:")
                    code_lines.extend(self.parse_json_structure(element['methods'], indentation_level + 1))
                    body_indentation = element['body'].replace('\\n', '\\n' + "    " * (indentation_level + 1))
                    code_lines.append("    " * (indentation_level + 1) + f"{body_indentation}")
            else:
                # Handle raw code lines and preserve blank lines
                code_lines.extend(["    " * indentation_level + line for line in element.split('\\n')])
        return code_lines

    def write_to_python_file(self, code_lines):
        with open(self.python_file_path, 'w') as file:
            file.write('\n'.join(code_lines))

    def convert_json_to_code(self):
        json_structure = self.read_json_file()
        parsed_code_lines = self.parse_json_structure(json_structure)
        self.write_to_python_file(parsed_code_lines)

if __name__ == "__main__":
    json_file_path = 'rna_dna_structure.json'  # Path to JSON file
    python_file_path = 'sim_dna.py'  # Output Python file path

    converter = JsonToCodeConverter(json_file_path, python_file_path)
    converter.convert_json_to_code()
