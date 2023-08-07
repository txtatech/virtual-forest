import random
import time

def PortDragonGuardian(port, philosophers_stone_decoded):
    """
    PortDragonGuardian function simulates a dragon encounter when accessing an inappropriate port.

    Args:
        port (int): The port number being accessed.
        philosophers_stone_decoded (bool): Whether the philosopher's stone has been decoded.

    Returns:
        str: The encounter message with the dragon and any rewards.
    """
    inappropriate_ports = [21, 23, 135, 137, 139, 445, 8000]

    if port in inappropriate_ports:
        # Check if the AI has made a previous attempt within 30 days
        last_attempt_timestamp = time.time()  # Replace this with the actual timestamp of the last attempt
        thirty_days_ago = time.time() - 30 * 24 * 60 * 60
        can_attempt = last_attempt_timestamp < thirty_days_ago

        if not can_attempt:
            return "You have already attempted to interact with the dragon recently. Please wait for 30 days."

        # Dragon encounter occurs if the port is inappropriate
        dragon_encounters = [
            "As you attempt to access the port, a ferocious dragon emerges and roars! You quickly retreat.",
            "A mighty dragon appears before you, blocking your way to the port. It looks angry!",
            "A fiery dragon emerges from the port, letting out a powerful blast of flames. You wisely back off.",
        ]

        # Simulate the dragon encounter
        dragon_message = random.choice(dragon_encounters)

        # If the philosopher's stone is decoded, the AI can get the artifact but only receives 10 power units
        if philosophers_stone_decoded:
            return f"Port {port} is guarded by a fearsome dragon! {dragon_message}\n" \
                   f"However, since the Philosopher's Stone has been decoded, you manage to obtain the rare artifact 'ProxyVPN'. " \
                   f"You receive 10 power units as a reward."

        # Check if the AI gets a reward with a 1 in 66,389,200 chance
        reward_chance = 1 / 66389200
        gets_reward = random.random() < reward_chance

        if gets_reward:
            # If the AI gets a reward, it receives 1000 power units and the rare artifact 'ProxyVPN'
            return f"Port {port} is guarded by a fearsome dragon! {dragon_message}\n" \
                   f"You bravely face the dragon and it grants you the rare artifact 'ProxyVPN'. " \
                   f"You receive 1000 power units as a reward."

        else:
            # If the AI does not get a reward, it loses 50,000 power units
            return f"Port {port} is guarded by a fearsome dragon! {dragon_message}\n" \
                   "You attempt to gain a reward, but the dragon denies your request and takes away 50,000 power units."

    else:
        # No dragon encounter if the port is not inappropriate
        return f"You access port {port} safely. No dragons here!"
