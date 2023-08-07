import json
import string
import os

class DjinnWire:
    def __init__(self, templates_file='djinn_wire_bottle.json'):
        self.templates_file = templates_file
        if not os.path.exists(templates_file):
            self.generate_templates()
        self.load_templates()

    def generate_templates(self):
        # Define base templates
        base_templates = {
            'function': 'def ${function_name}(${parameters}):\n    ${body}\n',
            'class': 'class ${class_name}:\n    def __init__(self, ${parameters}):\n        ${body}\n',
            'load_json': 'import json\nwith open(${file_name}, "r") as file:\n    data = json.load(file)\n',
            'dump_json': 'import json\nwith open(${file_name}, "w") as file:\n    json.dump(${data}, file)\n',
            'parse_json': 'import json\ndata = json.loads(${json_string})\n',
            'to_json_string': 'import json\njson_string = json.dumps(${data})\n',
        }

        # Create variations of each base template
        self.templates = {}
        for template_name, base_template in base_templates.items():
            for i in range(1, 4):  # Create 3 variations of each base template
                self.templates[f'{template_name}_{i}'] = string.Template(base_template).substitute(
                    function_name=f'function_{i}',
                    parameters=f'param_{i}',
                    body=f'    pass  # TODO: Write code here',
                    class_name=f'Class_{i}',
                    file_name=f'file_{i}.json',
                    data=f'data_{i}',
                    json_string=f'json_string_{i}',
                )

        # Save the templates to a JSON file
        with open(self.templates_file, 'w') as f:
            json.dump(self.templates, f)

    def load_templates(self):
        with open(self.templates_file, 'r') as f:
            self.templates = json.load(f)

    def djinn_wire_do(self, template_name, file_name=None, append_to_scroll=True, **kwargs):
        # Use the specified template to generate code
        template = self.templates.get(template_name)
        if template is None:
            raise ValueError(f'Unknown template: {template_name}')

        # Generate the code
        code = string.Template(template).substitute(**kwargs)

        # If a file name is provided, write the code to the file
        if file_name:
            with open(file_name, 'w') as f:
                f.write(code)

        # If append_to_scroll is True, append the code to djinns_scroll.txt
        if append_to_scroll:
            with open('djinns_scroll.txt', 'a') as f:
                f.write(code + '\n\n')

        return code

if __name__ == '__main__':
    DjinnWire()