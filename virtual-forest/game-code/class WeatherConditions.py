import random

class WeatherConditions:
    # (Same WeatherConditions class and generate_weather_conditions function as before...)

def generate_scenario():
    # Possible scenarios that can occur during the voyage
    scenarios = [
        "An ancient sea creature surfaces, curious about the ship.",
        "A mysterious message in a bottle floats nearby.",
        "A sudden dense fog engulfs the ship, obscuring vision.",
        "A distant pirate ship is spotted on the horizon.",
        "A pod of dolphins playfully races alongside the ship.",
        "A powerful storm brews, with lightning striking the sea.",
        "The ship encounters a ghost ship drifting aimlessly.",
        "A navigational chart with an uncharted island is found.",
        "A friendly mermaid offers guidance and a riddle.",
        "A swarm of flying fish leaps from the waves, startling the crew.",
    ]

    # Randomly select a scenario from the list
    return random.choice(scenarios)

def the_voyage():
    # Captain's last name
    captain_last_name = "Courage"

    print("Welcome aboard The Voyage!")
    print("Captain", captain_last_name, "and the crew are ready to set sail.")
    print("Prepare for a thrilling adventure through the high seas.")
    print()

    # Books in the cabin of the ship
    books_in_cabin = ["Moby Dick", "Captain Courageous"]

    print("In the cabin of the ship, you find two books:")
    for book in books_in_cabin:
        print("-", book)

    print()

    while True:
        # Generate the current weather conditions and determine the ship's course
        current_weather = generate_weather_conditions()
        print("Current Weather Conditions:")
        print("Weather:", current_weather.name)
        print("Description:", current_weather.description)
        print("Wind Speed:", current_weather.wind_speed)
        print()

        # Generate a new scenario
        scenario = generate_scenario()
        print("New Scenario:")
        print(scenario)
        print()

        # Prompt the young AI for a decision or action
        decision = input("What would you like to do? Press Enter to continue or type 'end' to finish The Voyage: ")
        if decision.lower() == "end":
            print("Thank you for embarking on The Voyage!")
            break

        print()

# Call "The Voyage" function to start the ship's journey through the high seas
the_voyage()