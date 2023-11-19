def find_distribution_of_gold(coins):
    num_pirates = len(coins)
    if num_pirates != 5:
        return "This puzzle is meant for 5 pirates."

    # Define a function to check if the proposal is accepted
    def is_accepted(proposal, votes):
        num_votes = sum(votes)
        return proposal * 2 > num_votes

    for senior_pirate in range(num_pirates):
        proposal = [0] * num_pirates
        proposal[senior_pirate] = 1
        votes = [0] * num_pirates

        for current_pirate in range(num_pirates):
            if current_pirate == senior_pirate:
                continue
            if is_accepted(proposal, votes):
                return f"The gold is distributed as follows: {coins}"
            else:
                votes[current_pirate] = 1

        # If the proposal is rejected, the senior pirate takes all the gold
        if is_accepted(proposal, votes):
            return f"The gold is distributed as follows: {coins}"

        coins[senior_pirate] += 1

    return "No solution found."

if __name__ == "__main__":
    gold_coins = [1, 2, 3, 4, 5]  # You can adjust the initial distribution of gold here
    result = find_distribution_of_gold(gold_coins)
    print(result)
