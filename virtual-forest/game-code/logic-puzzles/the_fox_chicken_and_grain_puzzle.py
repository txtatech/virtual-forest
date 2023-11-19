def solve_fox_chicken_grain_puzzle():
    left_bank = ["farmer", "fox", "chicken", "grain"]
    right_bank = []

    def is_valid_state(bank):
        # Check if the chicken and fox or chicken and grain are left alone
        if ("chicken" in bank and "fox" in bank) or ("chicken" in bank and "grain" in bank):
            return False
        return True

    def is_goal_state(bank):
        return bank == ["farmer", "fox", "chicken", "grain"]

    def move(state, item):
        new_state = state.copy()
        new_state.remove("farmer")
        new_state.remove(item)
        return new_state

    def print_state(bank):
        print("Left Bank: ", bank)

    def search(bank, path):
        if is_goal_state(bank):
            print("Solution found!")
            for step in path:
                print_state(step)
            return True

        for item in bank:
            if item != "farmer":
                new_bank = bank.copy()
                new_bank.remove("farmer")
                new_bank.remove(item)

                if is_valid_state(new_bank):
                    path.append(new_bank)
                    if search(new_bank, path):
                        return True
                    path.pop()

    print("Solving the Fox, Chicken, and Grain Puzzle...")
    path = [left_bank]
    search(left_bank, path)

if __name__ == "__main__":
    solve_fox_chicken_grain_puzzle()
