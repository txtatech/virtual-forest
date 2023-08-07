import chess
import chess.engine
import time

def print_chessboard(chessboard):
    print("   a b c d e f g h")
    print("  +-----------------+")
    for i in range(8):
        print(f"{8-i} | {' '.join(chessboard[i])} | {8-i}")
    print("  +-----------------+")
    print("   a b c d e f g h")

def initialize_chessboard():
    chessboard = [[' ' for _ in range(8)] for _ in range(8)]

    # Place pieces on the chessboard
    chessboard[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    chessboard[1] = ['P'] * 8
    chessboard[6] = ['p'] * 8
    chessboard[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

    return chessboard

def get_user_move():
    move = input("Enter your move in algebraic notation (e.g., e2e4): ")
    return chess.Move.from_uci(move)

def get_computer_move(chessboard):
    # Use a chess engine to get the computer's move
    with chess.engine.SimpleEngine.popen_uci("stockfish") as engine:
        result = engine.play(chessboard, chess.engine.Limit(time=2.0))
        return result.move

def make_move(chessboard, move, player_turn):
    if player_turn:
        # Implement move validation and make the player's move on the chessboard
        # For simplicity, let's assume the user always enters a valid move.
        chessboard.push(move)
    else:
        # Make the computer's move on the chessboard
        move_uci = get_computer_move(chessboard)
        chessboard.push(move_uci)

def play_game():
    chessboard = initialize_chessboard()
    player_turn = True

    while True:
        print_chessboard(chessboard)

        if player_turn:
            move = get_user_move()
        else:
            move = get_computer_move(chessboard)
            print(f"Computer plays: {move.uci()}")

        make_move(chessboard, move, player_turn)

        # Check for game over conditions and break the loop if necessary
        if chessboard.is_game_over():
            result = chessboard.result()
            if result == "1-0":
                print("Congratulations! You win!")
            elif result == "0-1":
                print("The computer wins!")
            else:
                print("It's a draw!")
            break

        # Switch player's turn
        player_turn = not player_turn

if __name__ == "__main__":
    play_game()
