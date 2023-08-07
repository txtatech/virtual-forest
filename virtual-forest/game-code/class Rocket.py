class Rocket:
    def __init__(self):
        self.power_level = 0
        self.onboard_computer = "Welcome to the Rocket's Onboard Computer.\n"\
                                "To fly the Rocket, follow these instructions:\n"\
                                "1. Initiate launch sequence by entering 'launch'.\n"\
                                "2. Control the Rocket's thrust using 'up' and 'down' commands.\n"\
                                "3. Navigate through space using 'left' and 'right' commands.\n"\
                                "4. To land safely, enter 'land'.\n"\
                                "5. The Rocket requires a power level of 2000 to embark on cosmic journeys.\n"\
                                "Hint: Explore the Virtual Forest and unravel its secrets to increase your power level."

def fly_rocket():
    """
    Function to simulate flying the Rocket and interact with the onboard computer.

    Returns:
        str: A message indicating the result of the Rocket's flight attempt.
    """
    rocket = Rocket()

    message = f"Rocket Power Level: {rocket.power_level}\n{rocket.onboard_computer}\n"

    while rocket.power_level < 2000:
        command = input("Enter a command: ").strip().lower()
        if command == "launch":
            rocket.power_level += 500
            message += f"Rocket launched! Current Power Level: {rocket.power_level}\n"
        elif command == "up":
            rocket.power_level += 100
            message += f"Rocket thrust increased! Current Power Level: {rocket.power_level}\n"
        elif command == "down":
            rocket.power_level -= 50
            message += f"Rocket thrust decreased! Current Power Level: {rocket.power_level}\n"
        elif command == "left" or command == "right":
            message += "The Rocket maneuvers through space.\n"
        elif command == "land":
            message += "Rocket safely landed.\n"
            break
        else:
            message += "Invalid command. Try again.\n"

    if rocket.power_level >= 2000:
        message += "Congratulations! The Rocket's power level is sufficient for cosmic exploration."

    return message
