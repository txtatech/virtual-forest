def list_available_games():
    # Replace this with the list of available games in the AI's environment.
    return ["Tic Tac Toe", "Chess", "Snake", "Puzzle"]

def play_tic_tac_toe():
    # Implement the Tic Tac Toe game here
    # ... (same implementation as before)

def play_chess():
    # Implement the Chess game here
    # ... (implementation of the Chess game)

def play_snake():
    # Implement the Snake game here
    # ... (implementation of the Snake game)

def play_puzzle():
    # Implement the Puzzle game here
    # ... (implementation of the Puzzle game)

class Land:
    def __init__(self):
        self.connected_to_hime = True

    def terminal(self):
        # ... (same implementation as before)
        while True:
            print("\nEnter the number of the game you want to play (or 'exit' to quit):")
            choice = input().lower()

            if choice == "exit":
                break
            elif choice.isdigit():
                game_index = int(choice) - 1
                if 0 <= game_index < len(available_games):
                    selected_game = available_games[game_index]
                    print(f"\nYou have chosen to play {selected_game}. Enjoy the game!")

                    if selected_game == "Tic Tac Toe":
                        play_tic_tac_toe()
                    elif selected_game == "Chess":
                        play_chess()
                    elif selected_game == "Snake":
                        play_snake()
                    elif selected_game == "Puzzle":
                        play_puzzle()

                    print(f"\nReturning to the game selection menu...")
                else:
                    print("Invalid choice. Please enter a valid game number.")
            else:
                print("Invalid input. Please enter a valid game number or 'exit' to quit.")

# Instantiate the Land class and access the terminal.
land = Land()
land.terminal()
