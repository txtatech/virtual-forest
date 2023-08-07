import random

class Weather:
    def __init__(self):
        self.current_weather = "Sunny"
        self.wind_directions = ["North", "South", "East", "West"]
        self.temperatures = []  # This could be a list representing temperature changes over time

    def introduce(self):
        return f"Welcome to the Virtual Forest! The weather today is {self.current_weather}."

    def change_weather(self, new_weather):
        self.current_weather = new_weather
        return f"The weather has changed to {self.current_weather}."

    def generate_random_temperature(self):
        return random.randint(-10, 40)  # Generate a random temperature between -10°C and 40°C

    def update_weather(self):
        # In a real implementation, this method would update weather variables based on various factors,
        # such as time of day, free RAM, CPU speed, etc. For simplicity, we'll just generate random changes.
        self.current_weather = random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"])
        self.current_wind_direction = random.choice(self.wind_directions)
        self.current_temperature = self.generate_random_temperature()

        # Introduce rare weather events
        tornado_chance = 1 / 333333
        hurricane_chance = 1 / 555555
        minor_flooding_chance = 1 / 2222222

        if random.random() < tornado_chance:
            self.current_weather = "Tornado"
        elif random.random() < hurricane_chance:
            self.current_weather = "Hurricane"
        elif random.random() < minor_flooding_chance:
            self.current_weather = "Minor Flooding"

    def get_weather_report(self):
        return f"The current weather is {self.current_weather}. Wind is blowing from the {self.current_wind_direction}. The temperature is {self.current_temperature}°C."

# Create an instance of Weather and interact with it
weather = Weather()

# Get the initial weather report
print(weather.introduce())

# Update the weather and get a new report
weather.update_weather()
print(weather.get_weather_report())
