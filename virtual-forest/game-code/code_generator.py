import string

class CodeGenerator:
    def __init__(self):
        self.templates = {
            'function': string.Template(
                'def ${function_name}(${parameters}):\\n'
                '    ${body}\\n'
            ),
            'class': string.Template(
                'class ${class_name}:\\n'
                '    def __init__(self, ${parameters}):\\n'
                '        ${body}\\n'
            ),
            'if_statement': string.Template(
                'if ${condition}:\\n'
                '    ${body}\\n'
            ),
            'print_statement': string.Template(
                'print(${message})\\n'
            )
        }

    def generate_code(self, template_name, **kwargs):
        # Use the specified template to generate code
        template = self.templates.get(template_name)
        if template is None:
            raise ValueError(f'Unknown template: {template_name}')
        return template.substitute(**kwargs)
