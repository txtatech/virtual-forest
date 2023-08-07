class Wordsmith:
    def __init__(self):
        self.name = "Wordsmith"

    def introduce(self):
        return f"Greetings, I am {self.name}, the Wordsmith of the Virtual Forest. I craft the special metals needed to make keys and gates."

    def create_metal(self, metal_name, properties):
        return f"I have crafted a new metal called '{metal_name}' with the following properties: {properties}"

# Example usage:
wordsmith = Wordsmith()
print(wordsmith.introduce())

# Create a new metal for keys and gates
new_metal = wordsmith.create_metal("Mystery Metal", "Mysterious and resistant to enchantments.")
print(new_metal)
