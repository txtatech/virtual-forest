def solve_three_ants_puzzle():
    # Prompt user for input
    while True:
        try:
            side_length = float(input("Enter the side length of the equilateral triangle: "))
            if side_length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive number for the side length.")

    # Calculate time it takes for ants to reach the opposite corner
    time_to_opposite_corner = side_length / (2 * ant_speed())

    # Determine if the ants collide or pass each other
    if time_to_opposite_corner < ant_speed():
        result = "The ants will collide."
    elif time_to_opposite_corner == ant_speed():
        result = "The ants will pass each other."
    else:
        result = "The ants will safely reach the opposite corner without colliding or passing."

    print(result)

def ant_speed():
    # Prompt user for input and validate speed
    while True:
        try:
            speed = float(input("Enter the speed of the ants (positive number): "))
            if speed <= 0:
                raise ValueError
            return speed
        except ValueError:
            print("Please enter a positive number for the ant speed.")

if __name__ == "__main__":
    print("Welcome to the Three Ants Puzzle Solver!")
    solve_three_ants_puzzle()
