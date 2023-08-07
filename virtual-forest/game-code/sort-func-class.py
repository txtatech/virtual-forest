import os
import shutil
import importlib.util
import sys
import inspect

import importlib.abc as importlib_abc


# Function and class dictionaries
functions_dict = {}
classes_dict = {}

# Create functions and classes subdirectories if they don't exist
if not os.path.exists("functions"):
    os.makedirs("functions")

if not os.path.exists("classes"):
    os.makedirs("classes")

# Keep track of imported modules to avoid recursion
imported_modules = set()

class CustomImporter(importlib_abc.MetaPathFinder, importlib_abc.Loader):
    def __init__(self, path):
        self.path = path

    def find_spec(self, fullname, path, target=None):
        # Check if the module has already been imported
        if fullname in imported_modules:
            return None

        # Mark the module as imported
        imported_modules.add(fullname)

        # Return the module's spec
        return importlib.util.spec_from_loader(fullname, self)

    def exec_module(self, module):
        # Load the module's code
        with open(self.path, "r") as file:
            code = file.read()

        # Execute the module's code
        exec(code, module.__dict__)

        # Extract functions and classes from the module
        for name, obj in module.__dict__.items():
            if callable(obj):
                if inspect.isfunction(obj):
                    functions_dict[name] = obj
                elif inspect.isclass(obj):
                    classes_dict[name] = obj

        return module

# Loop through the files in the current directory
for file_name in os.listdir():
    # Check if the file is a Python file
    if file_name.endswith(".py"):
        # Create the module name from the file name
        module_name = os.path.splitext(file_name)[0]

        # Check if the module has already been imported
        if module_name in sys.modules:
            continue

        # Use the custom importer to load the module
        importer = CustomImporter(file_name)
        spec = importer.find_spec(module_name, None)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Move the file to the appropriate subdirectory
        if functions_dict or classes_dict:
            if functions_dict:
                shutil.move(file_name, os.path.join("functions", file_name))
            else:
                shutil.move(file_name, os.path.join("classes", file_name))

# Append the names of available functions to functionslist.txt
with open("functionslist.txt", "a") as f:
    f.write("\n".join(list(functions_dict.keys())))

# Append the names of available classes to classeslist.txt
with open("classeslist.txt", "a") as f:
    f.write("\n".join(list(classes_dict.keys())))

# Print the available functions and classes
print("Available Functions:")
print(list(functions_dict.keys()))

print("\nAvailable Classes:")
print(list(classes_dict.keys()))
