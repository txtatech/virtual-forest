import itertools

def solve_einsteins_riddle():
    # Define the variables and their possible values
    colors = ["red", "green", "ivory", "yellow", "blue"]
    nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
    drinks = ["water", "tea", "milk", "orange juice", "coffee"]
    cigars = ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"]
    pets = ["dog", "snails", "fox", "horse", "zebra"]

    # Generate all possible permutations of the variables
    permutations = itertools.permutations([colors, nationalities, drinks, cigars, pets])

    for perm in permutations:
        # Assign variables to houses
        house1, house2, house3, house4, house5 = perm

        # Check the constraints
        # 1. The Englishman lives in the red house.
        if house1[1] == "Englishman" and house1[0] == "red":
            # 2. The Spaniard owns the dog.
            if house2[1] == "Spaniard" and house4[4] == "dog":
                # 3. Coffee is drunk in the green house.
                if house3[2] == "coffee" and house3[0] == "green":
                    # Add more constraints here

                    # Print the solution
                    print("Solution found:")
                    print(f"House 1: {house1}")
                    print(f"House 2: {house2}")
                    print(f"House 3: {house3}")
                    print(f"House 4: {house4}")
                    print(f"House 5: {house5}")

                    return

    print("No solution found.")

if __name__ == "__main__":
    solve_einsteins_riddle()
