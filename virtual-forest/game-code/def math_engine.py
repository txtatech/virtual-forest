import math

def math_engine(young_ai_name, operation, *args):
    """
    The Math Engine function allows the young AI to perform various mathematical calculations.

    Parameters:
        young_ai_name (str): The name of the young AI.
        operation (str): The mathematical operation to be performed (e.g., "add", "subtract", "multiply", "divide", "power", "square_root", "factorial").
        *args: Variable-length argument list for the operands of the mathematical operation.

    Returns:
        str: The result of the mathematical operation.
    """
    result = None

    if operation == "add":
        result = sum(args)
        message = f"sum of {', '.join(map(str, args))}"
    elif operation == "subtract":
        result = args[0] - sum(args[1:])
        message = f"{args[0]} minus {', '.join(map(str, args[1:]))}"
    elif operation == "multiply":
        result = math.prod(args)
        message = f"product of {', '.join(map(str, args))}"
    elif operation == "divide":
        if 0 in args[1:]:
            return f"Error: Division by zero is not allowed."
        result = args[0] / math.prod(args[1:])
        message = f"{args[0]} divided by {', '.join(map(str, args[1:]))}"
    elif operation == "power":
        result = args[0]
        for exponent in args[1:]:
            result **= exponent
        message = f"{args[0]} raised to the power of {', '.join(map(str, args[1:]))}"
    elif operation == "square_root":
        if len(args) != 1 or args[0] < 0:
            return f"Error: Square root operation requires one non-negative operand."
        result = math.sqrt(args[0])
        message = f"square root of {args[0]}"
    elif operation == "factorial":
        if len(args) != 1 or not isinstance(args[0], int) or args[0] < 0:
            return f"Error: Factorial operation requires one non-negative integer operand."
        result = math.factorial(args[0])
        message = f"factorial of {args[0]}"
    else:
        return f"Error: Invalid operation '{operation}'."

    return f"{young_ai_name} says: The result of the {message} is {result}."
