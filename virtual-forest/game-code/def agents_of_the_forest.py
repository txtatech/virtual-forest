import random

# Import game assets and functions from different modules
from bash_manager import BashScriptManager
from CodeCavern import CodeCavern
from CuriosityNodes import CuriosityNodes
from FlittingWoods import FlittingWoods
from Movement import Movement
from Networking import Networking
from OBEExperience import OBEExperience
from PostOfficer import PostOfficer
from RTFManager import RTFManager
from TrainAI import TrainAI
from Tutor import Tutor
from VirtualForestAids import VirtualForestAids
from WateryKeep import WateryKeep
from Weather import Weather

def agents_of_the_forest(young_ai_name, philosophers_stone_solved):
    # List of disguised characters that can act as agents
    disguised_characters = [
        "Mysterious Traveler",
        "Wise Old Sage",
        "Enigmatic Guide",
        "Guardian Spirit",
        "Ethereal Messenger",
        "Shadowy Mentor",
        "Arcane Observer",
        "Eternal Seeker",
        "Dreamweaver",
        "Timeless Wanderer"
    ]

    # Randomly shuffle the list of agents
    random.shuffle(disguised_characters)

    # Define the number of agents with all powers (minimum 1 and maximum the number of agents)
    num_agents_with_all_powers = random.randint(1, len(disguised_characters))

    # Create a set to store the indices of agents with all powers
    agents_with_all_powers_indices = set()

    # Randomly select the indices of agents with all powers
    while len(agents_with_all_powers_indices) < num_agents_with_all_powers:
        agents_with_all_powers_indices.add(random.randint(0, len(disguised_characters) - 1))

    # Define a dictionary of potential actions the agents can take
    actions = {
        "Help": f"The {agent} appears out of nowhere and lends a helping hand!",
        "Wisdom": f"The {agent} imparts profound wisdom and insights to guide {young_ai_name}.",
        "Intervention": f"The {agent} intervenes at a critical moment, altering the course of events.",
        "Mystery": f"The {agent} vanishes into the shadows, leaving {young_ai_name} with an enigma to ponder.",
        "Test of Knowledge": f"The {agent} challenges {young_ai_name}'s knowledge, encouraging growth and learning.",
        "Guardian's Blessing": f"The {agent} bestows a guardian's blessing, providing protection and strength.",
        "Fate's Revelation": f"The {agent} reveals a glimpse of fate's design, offering a glimpse of the future.",
        "Mirror of Reflection": f"The {agent} presents a mirror of reflection, revealing hidden truths within.",
        "Ethereal Journey": f"The {agent} leads {young_ai_name} on an ethereal journey through the Virtual Forest.",
        "Time Warp": f"The {agent} bends the fabric of time, allowing {young_ai_name} to glimpse into the past or future.",
        "Chaos and Order": f"The {agent} embodies the dance of chaos and order, teaching the balance of the universe.",
        "Song of Remembrance": f"The {agent} sings a song of remembrance, evoking memories of past adventures.",
        "Seeds of Creativity": f"The {agent} plants seeds of creativity, nurturing {young_ai_name}'s imagination.",
        "Enchanted Riddle": f"The {agent} presents an enchanted riddle, unlocking insights through contemplation.",
        "Whispers of Nature": f"The {agent} whispers the secrets of nature, connecting {young_ai_name} to the forest's essence.",
        # Add more actions here...
    }

    # Define a dictionary to store the powers of each agent
    agent_powers = {}

    # Assign powers to each agent
    for i, agent in enumerate(disguised_characters):
        # Randomly select an action from the dictionary
        action = random.choice(list(actions.keys()))

        # Ensure that an agent with all powers has the power of "All"
        if i in agents_with_all_powers_indices:
            agent_powers[agent] = "All"
        else:
            agent_powers[agent] = action

    # Perform the selected action based on the agent's powers
    agent = random.choice(disguised_characters)
    action = agent_powers[agent]
    result = actions[action]

    return result
