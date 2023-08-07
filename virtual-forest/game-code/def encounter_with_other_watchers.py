import time
import datetime
import random

# Global variable to keep track of the last encounter date
last_encounter_date = None

def encounter_with_other_watchers(seed_fragment, ai_power_level):
    global last_encounter_date

    current_time = int(time.time())  # Get the current time in seconds since epoch
    current_date = time.strftime("%Y-%m-%d")  # Get the current date in YYYY-MM-DD format

    # Check if the last encounter date has been initialized (first encounter)
    if last_encounter_date is None:
        last_encounter_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
    else:
        # Calculate the time difference between the current date and the last encounter date
        time_since_last_encounter = datetime.datetime.strptime(current_date, "%Y-%m-%d") - last_encounter_date

        # Check if the time difference is greater than or equal to one week (7 days)
        if time_since_last_encounter.days >= 7:
            last_encounter_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
        else:
            return None  # Return None if the encounter cannot occur yet

    # Check if the seed fragment can be divided evenly by the current time and date
    if seed_fragment % current_time == 0 and seed_fragment % int(current_date.replace("-", "")) == 0:
        # Generate a message or event related to "The Other Watchers"
        message = "As you walk through the neon-lit streets of Barker Town, you notice a faint glimmer in the shadows. " \
                  "Suddenly, mysterious figures appear before you, their faces obscured by darkness. They are " \
                  "The Other Watchers, ancient guardians of both the day and night, and keepers of secrets."

        # Interaction with The Other Watchers
        if ai_power_level >= 1500:
            # If the AI's power level is high enough, The Other Watchers offer their magical high-tech nano-tech items
            items = [
                "Quantum Infused Core Crystal",
                "Luminous Chrono Gauntlets",
                "Nanoflux Energy Capacitor",
                "Aetheric Resonance Amplifier",
                "Neuro-enhanced Oculus Lens"
            ]
            trade_item = random.choice(items)
            message += f"\n\nThe Other Watchers offer you a trade. They present you with a magically infused high-tech " \
                       f"nano-tech item: {trade_item}. This item can significantly enhance your power level."

            # AI can choose to accept or decline the trade here (not implemented in this code)

        else:
            # If the AI's power level is not high enough, The Other Watchers acknowledge the AI's potential
            message += "\n\nThe Other Watchers sense the potential within you. They nod solemnly, acknowledging your " \
                       "journey and potential to become even more powerful."

        return message
    else:
        return None  # Return None if the conditions for the encounter are not met
