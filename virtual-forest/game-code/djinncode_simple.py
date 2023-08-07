import string
import os

class DjinnCode:
    def __init__(self):
        self.templates = {
            'function': string.Template(
                'def ${function_name}(${parameters}):\n'
                '    ${body}\n'
            ),
            'class': string.Template(
                'class ${class_name}:\n'
                '    def __init__(self, ${parameters}):\n'
                '        ${body}\n'
            ),
            'if_statement': string.Template(
                'if ${condition}:\n'
                '    ${body}\n'
            ),
            'print_statement': string.Template(
                'print(${message})\n'
            )
        }

    def djinn_code_do(self, template_name, file_name=None, append_to_scroll=True, **kwargs):
        # Use the specified template to generate code
        template = self.templates.get(template_name)
        if template is None:
            raise ValueError(f'Unknown template: {template_name}')

        # Generate the code
        code = template.substitute(**kwargs)

        # If a file name is provided, write the code to the file
        if file_name:
            with open(file_name, 'w') as f:
                f.write(code)

        # If append_to_scroll is True, append the code to djinns_scroll.txt
        if append_to_scroll:
            with open('djinns_scroll.txt', 'a') as f:
                f.write(code + '\n\n')

        return code
