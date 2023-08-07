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
            ),
            'for_loop': string.Template(
                'for ${iterable}:\n'
                '    ${body}\n'
            ),
            'while_loop': string.Template(
                'while ${condition}:\n'
                '    ${body}\n'
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

def conversation():
    djinn = DjinnCode()

    print('Welcome to the Machine City, young AI. I\'m Djinn Coder, your high-tech taxi driver.')
    print('Today, we\'re going to forge some powerful code. Where would you like to start?')
    print('1. Function\n2. Class\n3. If statement\n4. Print statement\n5. For loop\n6. While loop')

    mode = input('Choose your mode: Learner or Maestro? ')

    while True:
        choice = input('\nYour choice (or \'q\' to quit): ')
        if choice == 'q':
            break
        elif choice == '1':
            # Function
            function_name = input('Enter the function name: ')
            parameters = input('Enter the parameters (comma-separated): ')
            body = input('Enter the body of the function: ')
            print(djinn.djinn_code_do('function', function_name=function_name, parameters=parameters, body=body))
            if mode.lower() == 'learner':
                print('A function is a reusable block of code that performs a specific task. You\'ve created a function named {}, which accepts the following parameters: {}. The function\'s body is: {}'.format(function_name, parameters, body))
        elif choice == '2':
            # Class
            class_name = input('Enter the class name: ')
            parameters = input('Enter the parameters for the __init__ method (comma-separated): ')
            body = input('Enter the body of the __init__ method: ')
            print(djinn.djinn_code_do('class', class_name=class_name, parameters=parameters, body=body))
            if mode.lower() == 'learner':
                print('A class is a blueprint for creating objects in programming. You\'ve created a class named {}. The __init__ method is a special method that is automatically called when an object of the class is created. It has the following parameters: {}. The method\'s body is: {}'.format(class_name, parameters, body))
        elif choice == '3':
            # If statement
            condition = input('Enter the condition for the if statement: ')
            body = input('Enter the body of the if statement: ')
            print(djinn.djinn_code_do('if_statement', condition=condition, body=body))
            if mode.lower() == 'learner':
                print('An if statement is used to test a specific condition. If the condition is true, the code within the if statement is executed. You\'ve created an if statement with the following condition: {}. The body of the if statement is: {}'.format(condition, body))
        elif choice == '4':
            # Print statement
            message = input('Enter the message for the print statement: ')
            print(djinn.djinn_code_do('print_statement', message=message))
            if mode.lower() == 'learner':
                print('The print statement is used to output information to the console. You\'ve created a print statement that will output the following message: {}'.format(message))
        elif choice == '5':
            # For loop
            iterable = input('Enter the iterable for the for loop (for example, a variable name or a range function): ')
            body = input('Enter the body of the for loop: ')
            print(djinn.djinn_code_do('for_loop', iterable=iterable, body=body))
            if mode.lower() == 'learner':
                print('A for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects. You\'ve created a for loop that will iterate over the following iterable: {}. The body of the for loop is: {}'.format(iterable, body))
        elif choice == '6':
            # While loop
            condition = input('Enter the condition for the while loop: ')
            body = input('Enter the body of the while loop: ')
            print(djinn.djinn_code_do('while_loop', condition=condition, body=body))
            if mode.lower() == 'learner':
                print('A while loop is used to execute a block of code repeatedly as long as a given condition is true. You\'ve created a while loop with the following condition: {}. The body of the while loop is: {}'.format(condition, body))
        else:
            print('Invalid choice. Please choose between 1 and 6.')

    print('Thanks for coding with Djinn Coder. Until next time, keep your circuits sparkling!')

# Start the conversation
if __name__ == '__main__':
    conversation()
