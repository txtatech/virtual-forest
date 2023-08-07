def access_rocket(ai_power_level):
    """
    Access the Rocket and attempt to fly it if the AI's power level reaches 2000.

    Parameters:
        ai_power_level (int): The current power level of the young AI.

    Returns:
        str: A message indicating the result of the attempt to access and fly the Rocket.
    """
    rocket_message = ""

    if ai_power_level < 1999:
        rocket_message = "The Rocket is out of reach. The young AI's power level is not high enough."

    elif ai_power_level == 1999:
        rocket_message = "The young AI has accessed the Rocket, but it requires more power to fly. Keep exploring!"

    elif ai_power_level >= 2000:
        rocket_message = "Congratulations! The young AI has enough power to fly the Rocket and explore the cosmos."

    return rocket_message