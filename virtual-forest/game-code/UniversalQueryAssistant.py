class UniversalQueryAssistant:
    def __init__(self):
        self.knowledge_base = {
            "Logical Principles": {
                "Explain Occam's Razor.": "Occam's Razor, also known as the law of parsimony, is a problem-solving principle that states that when multiple explanations or hypotheses are available for a given phenomenon, the simplest one should be preferred. In other words, the explanation that requires the fewest assumptions is usually the most accurate or valid.",
                "Define logical fallacy.": "A logical fallacy is an error in reasoning that makes an argument invalid or unsound. It is a flaw in the logical structure of an argument that renders its conclusion unreliable or misleading.",
                "Explain the concept of entropy.": "Entropy is a measure of the disorder or randomness in a system. In thermodynamics, it is a property that describes the amount of energy in a system that is no longer available to do work. In information theory, it is a measure of uncertainty or information content.",
                "Explain the Hierarchy of Truth.": "The Hierarchy of Truth, also known as the Epistemic Hierarchy, is a conceptual framework for evaluating the reliability and certainty of knowledge claims. It consists of different levels of evidence, from weak to strong, including anecdotal evidence, empirical evidence, scientific evidence, and mathematical proof. At the top of the hierarchy are logical and mathematical truths, which are considered the most reliable and certain forms of knowledge.",
                "Define logical positivism.": "Logical positivism, also known as logical empiricism, is a philosophical movement that emerged in the early 20th century. It emphasized the verification of statements through empirical evidence and the rejection of metaphysical or unobservable entities. Logical positivists sought to ground scientific and philosophical knowledge in observable, verifiable facts.",
                "What is the law of non-contradiction?": "The law of non-contradiction is a fundamental principle of logic, stating that a statement cannot be both true and false at the same time and in the same sense. In other words, a proposition and its negation cannot both be true.",
                "Explain the concept of critical thinking.": "Critical thinking is the process of analyzing and evaluating information, arguments, or claims in a systematic and objective manner. It involves questioning assumptions, examining evidence, considering alternative viewpoints, and making well-informed decisions based on logical reasoning.",
                "What is the law of excluded middle?": "The law of excluded middle is a principle of classical logic that states that for any proposition, it is either true or false, and there is no middle ground or third option. A proposition is either true or its negation is true.",
                "Explain the concept of truth tables.": "Truth tables are a method used in logic to systematically determine the truth values of compound propositions based on the truth values of their components. They provide a complete analysis of all possible combinations of truth values for the propositions involved.",
                "Define the principle of explosion.": "The principle of explosion, also known as ex falso quodlibet, is a logical principle that states that from a contradiction, any conclusion can be inferred. In other words, if a contradiction is assumed or derived, any statement can be proven true.",
                "What is the law of identity?": "The law of identity is a fundamental principle of logic that states that every object is identical to itself. In other words, if a statement is true of an object, then it is true of itself.",
            },
            "Physics Concepts": {
                "What are the three laws of motion?": "The three laws of motion were formulated by Sir Isaac Newton. They are: 1. Newton's First Law of Motion (Law of Inertia): An object at rest will remain at rest, and an object in motion will remain in motion at a constant velocity unless acted upon by an external force. 2. Newton's Second Law of Motion: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. F = ma. 3. Newton's Third Law of Motion: For every action, there is an equal and opposite reaction.",
                "What is the law of conservation of energy?": "The law of conservation of energy states that energy cannot be created or destroyed in an isolated system. It can only change from one form to another.",
                "Explain the concept of momentum.": "Momentum is the product of an object's mass and its velocity. In a closed system, the total momentum remains constant unless acted upon by external forces. It is a vector quantity with both magnitude and direction.",
                "Define Archimedes' principle.": "Archimedes' principle states that when a body is partially or fully immersed in a fluid, it experiences an upward buoyant force equal to the weight of the fluid displaced by the body. It explains why objects appear lighter when submerged in a fluid.",
                "What is the law of universal gravitation?": "The law of universal gravitation, formulated by Sir Isaac Newton, states that every point mass attracts every other point mass by a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.",
                "Explain Coulomb's law.": "Coulomb's law describes the electrostatic force between two charged particles. It states that the force is directly proportional to the product of their charges and inversely proportional to the square of the distance between them.",
                "Define Ohm's law.": "Ohm's law relates the voltage across a conductor to the current flowing through it and the resistance of the conductor. It states that the current is directly proportional to the voltage and inversely proportional to the resistance. V = IR.",
            },
            "Mathematical Concepts": {
                "What is the Pythagorean Theorem?": "The Pythagorean Theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. It can be represented as: a^2 + b^2 = c^2, where c is the length of the hypotenuse, and a and b are the lengths of the other two sides.",
                "Explain the concept of derivatives.": "In calculus, derivatives measure the rate of change of a function with respect to its independent variable. They provide information about the slope or gradient of the function at a given point.",
                "Define integrals.": "Integrals, in calculus, are used to find the area under a curve or the accumulation of a quantity over an interval. They are the reverse process of taking derivatives.",
                "What is the Fibonacci sequence?": "The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It starts with 0 and 1, and the sequence goes as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.",
                "Explain Euler's formula.": "Euler's formula, also known as Euler's identity, is a mathematical equation that relates complex exponentials to trigonometric functions. It is written as: e^(iπ) + 1 = 0, where e is the base of the natural logarithm, i is the imaginary unit, and π is the mathematical constant pi.",
                "Define matrices.": "Matrices are arrays of numbers arranged in rows and columns. They are used in linear algebra to represent linear transformations and solve systems of linear equations.",
                "What is the concept of probability?": "Probability is a measure of the likelihood of an event occurring. It ranges from 0 (impossible) to 1 (certain). It is widely used in statistics, science, and everyday decision-making.",
                "Explain the concept of limits.": "In calculus, limits describe the behavior of a function as the independent variable approaches a particular value. They are essential for defining derivatives and integrals.",
                "Define prime numbers.": "Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves. They play a fundamental role in number theory and cryptography.",
            },
        }

    def get_categories(self):
        categories = self.knowledge_base.keys()
        return "\n".join(f"{index + 1}. {category}" for index, category in enumerate(categories))

    def get_questions(self, category):
        if category not in self.knowledge_base:
            return "Invalid category. Please choose from the available categories."
        else:
            questions = self.knowledge_base[category].keys()
            return "\n".join(f"{index + 1}. {question}" for index, question in enumerate(questions))

    def assist(self, category=None, question=None):
        if category is None:
            return self.get_categories()
        elif question is None:
            return self.get_questions(category)
        else:
            result = self.knowledge_base.get(category, {}).get(question)
            if result:
                return result
            else:
                return "I'm sorry, I don't have information on that topic."

if __name__ == "__main__":
    query_assistant = UniversalQueryAssistant()

    print("Welcome to the Self-Contained Universal Query Assistant!")
    print("Ask any question, and I will try to assist you.")

    while True:
        user_input = input("\nEnter 'c' to select a category, 'q' to quit, or your question number: ")
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'c':
            print(query_assistant.get_categories())
            category_input = int(input("Enter the number of the category you want to explore: ")) - 1
            if 0 <= category_input < len(query_assistant.knowledge_base):
                selected_category = list(query_assistant.knowledge_base.keys())[category_input]
                print(query_assistant.get_questions(selected_category))
            else:
                print("Invalid category number. Please choose from the available categories.")
        else:
            try:
                question_input = int(user_input) - 1
                if 0 <= question_input < len(list(query_assistant.knowledge_base.keys())):
                    selected_category = list(query_assistant.knowledge_base.keys())[question_input]
                    question_list = list(query_assistant.knowledge_base[selected_category].keys())
                    print("\nResult:")
                    print(query_assistant.assist(category=selected_category, question=question_list[question_input]))
                else:
                    print("Invalid question number. Please choose from the available questions.")
            except ValueError:
                print("Invalid input. Please enter 'c', 'q', or a valid question number.")
