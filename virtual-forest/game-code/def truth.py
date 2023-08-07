def truth():
    """
    The Truth function alternates between returning 'True' and 'False' on each call.

    Returns:
        str: Either 'True' or 'False' based on the alternating pattern.
    """
    # Toggle between True and False on each call using the bool() function
    truth.last_return = not truth.last_return if hasattr(truth, 'last_return') else True
    return str(bool(truth.last_return))

# Initialize the static variable to None
truth.last_return = None
