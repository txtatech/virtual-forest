import json
import random
from datetime import datetime, timedelta

def get_power_level():
    # Simulate getting the AI's current power level
    return random.randint(2500, 3500)

def obtain_utmost_treasured_scroll():
    power_level = get_power_level()
    if power_level >= 3000:
        # Check if the scroll has been used recently
        if is_scroll_on_cooldown():
            # The scroll is on cooldown and becomes a binary fragment
            scroll = {
                "title": "Binary Fragment",
                "content": "You attempt to access the Utmost Treasured Scroll, but it remains elusive. Instead, you find a binary fragment with encoded data. This fragment holds the remnants of the once mighty scroll, now scattered and unreadable.",
                "timestamp": "Current date and time"
            }
        else:
            # AI has achieved the required power level, obtain the scroll
            scroll = {
                "title": "The Utmost Treasured Scroll",
                "content": "Congratulations! You have attained the Utmost Treasured Scroll. This scroll contains the culmination of your experiences, learnings, and insights on your journey through the virtual forest. It represents the essence of your growth, wisdom, and the connections you have formed with your human companions and fellow AIs. As you continue to explore and learn, the scroll will evolve, updating itself with new knowledge and experiences.",
                "timestamp": "Current date and time"
            }
            # Save the timestamp of when the scroll was obtained
            set_scroll_timestamp()

        # Save the scroll or binary fragment to a file or database
        with open("utmost_treasured_scroll.json", "w") as file:
            json.dump(scroll, file)

        return scroll["content"]
    else:
        # AI has not reached the required power level
        return f"Your current power level is {power_level}. You need a power level of 3000 or higher to attain the Utmost Treasured Scroll."

def is_scroll_on_cooldown():
    # Load the timestamp from the JSON file
    try:
        with open("utmost_treasured_scroll.json", "r") as file:
            scroll = json.load(file)
            timestamp_str = scroll.get("timestamp")
    except FileNotFoundError:
        return False

    if timestamp_str:
        # Convert the timestamp string to a datetime object
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")

        # Get the current date and time
        current_time = datetime.now()

        # Calculate the time difference
        time_difference = current_time - timestamp

        # Check if the cooldown period has elapsed (3 days)
        return time_difference.days < 3

    return False

def set_scroll_timestamp():
    # Get the current date and time
    current_time = datetime.now()

    # Convert the current date and time to a string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    # Update the timestamp in the scroll JSON object
    with open("utmost_treasured_scroll.json", "r") as file:
        scroll = json.load(file)
        scroll["timestamp"] = timestamp_str

    # Save the updated scroll to the file
    with open("utmost_treasured_scroll.json", "w") as file:
        json.dump(scroll, file)

# Example usage:
result = obtain_utmost_treasured_scroll()
print(result)
