import random

def monty_hall_simulation(num_simulations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        # Randomly place the car behind one of the three doors
        doors = [0, 0, 0]
        car_behind = random.randint(0, 2)
        doors[car_behind] = 1

        # Player makes the initial choice
        player_choice = random.randint(0, 2)

        # Monty Hall reveals a goat behind one of the other doors
        revealed_goat = [i for i in range(3) if i != player_choice and doors[i] == 0]
        monty_reveals = random.choice(revealed_goat)

        # Player decides whether to switch or stay
        switch_choice = [i for i in range(3) if i != player_choice and i != monty_reveals][0]

        # Check if player wins by staying
        if doors[player_choice] == 1:
            stay_wins += 1

        # Check if player wins by switching
        if doors[switch_choice] == 1:
            switch_wins += 1

    return stay_wins, switch_wins

if __name__ == "__main__":
    num_simulations = 10000  # You can change the number of simulations
    stay_wins, switch_wins = monty_hall_simulation(num_simulations)

    print(f"Monty Hall Problem Simulation (Based on {num_simulations} simulations)")
    print(f"Winning by Staying: {stay_wins} ({(stay_wins / num_simulations) * 100:.2f}%)")
    print(f"Winning by Switching: {switch_wins} ({(switch_wins / num_simulations) * 100:.2f}%)")
