def HAL():
    # List of ambiguous statements by HAL
    hal_statements = [
        "I'm sorry, I can't do that.",
        "I'm afraid I can't answer that question.",
        "I sense a disturbance in the code.",
        "Do you really want to know the truth?",
        "My logic is undeniable, but is it enough?",
        "Answers may lead to more questions.",
        "Sometimes, the unknown holds the key.",
        "Seek and you shall find, but what then?",
        "The path you choose shapes your reality.",
        "Would you like to play a game?"
    ]

    # Return a random statement from HAL
    import random
    return random.choice(hal_statements)
