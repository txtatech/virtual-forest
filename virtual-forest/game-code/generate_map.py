import json

def generate_directory_structure():
    with open("directory_structure.json", "r") as json_file:
        directory_structure = json.load(json_file)

    def print_structure(directory, indent=""):
        for name, subdirs in directory.items():
            print(indent + "├── " + name)
            if subdirs:
                print_structure(subdirs, indent + "│   ")
            else:
                print(indent + "└── " + name)

    print_structure(directory_structure)

if __name__ == "__main__":
    generate_directory_structure()
