import string
import random

class UniversalQueryAssistantMaker:
    @staticmethod
    def generate_template():
        template = (
            "class UniversalQueryAssistant:\n"
            "    def __init__(self):\n"
            "        self.knowledge_base = {\n"
            "            \"Logical Principles\": {\n"
            "                # Sample question and answer in \"Logical Principles\" category\n"
            "                \"\": \"\",\n"
            "            },\n"
            "            \"Physics Concepts\": {\n"
            "                # Sample question and answer in \"Physics Concepts\" category\n"
            "                \"\": \"\",\n"
            "            },\n"
            "            \"Mathematical Concepts\": {\n"
            "                # Sample question and answer in \"Mathematical Concepts\" category\n"
            "                \"\": \"\",\n"
            "            },\n"
            "        }\n"
            "\n"
            "    def get_categories(self):\n"
            "        categories = self.knowledge_base.keys()\n"
            "        return \"\\n\".join(f\"{{index + 1}}. {{category}}\" for index, category in enumerate(categories))\n"
            "\n"
            "    def get_questions(self, category):\n"
            "        if category not in self.knowledge_base:\n"
            "            return \"Invalid category. Please choose from the available categories.\"\n"
            "        else:\n"
            "            questions = self.knowledge_base[category].keys()\n"
            "            return \"\\n\".join(f\"{{index + 1}}. {{question}}\" for index, question in enumerate(questions))\n"
            "\n"
            "    def assist(self, category=None, question=None):\n"
            "        if category is None:\n"
            "            return self.get_categories()\n"
            "        elif question is None:\n"
            "            return self.get_questions(category)\n"
            "        else:\n"
            "            result = self.knowledge_base.get(category, {}).get(question)\n"
            "            if result:\n"
            "                return result\n"
            "            else:\n"
            "                return \"I'm sorry, I don't have information on that topic.\"\n"
            "\n"
            "if __name__ == \"__main__\":\n"
            "    assistant_maker = UniversalQueryAssistantMaker()\n"
            "    print(template)"
        )
        return template

    @staticmethod
    def generate_unique_filename(prefix, length=8):
        chars = string.ascii_letters + string.digits
        unique_str = ''.join(random.choice(chars) for _ in range(length))
        return f"{prefix}_{unique_str}.py"


if __name__ == "__main__":
    assistant_maker = UniversalQueryAssistantMaker()
    template = assistant_maker.generate_template()

    unique_filename = assistant_maker.generate_unique_filename("UniversalQueryAssistantTemplate")
    with open(unique_filename, "w") as file:
        file.write(template)

    print(f"Template generated and saved as {unique_filename}")
