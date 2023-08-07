import random
import time

def generate_maze(completed_guardian_scene):
    # Check if the Guardian Scene is completed
    if completed_guardian_scene:
        # Generate a random number from 1 to 10100101
        rand_num = random.randint(1, 10100101)

        # Determine if an artifact should spawn based on the random number
        artifact_spawn_chance = 1
        artifact_spawns = rand_num % artifact_spawn_chance == 0

        # Create the maze with the artifact (if it spawns)
        if artifact_spawns:
            # Your code to generate a maze with the artifact at its center goes here
            # For example, you can use a 2D array to represent the maze

            # Placeholder code for illustration purposes
            maze = [
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ]

            # Place the artifact at the center of the maze
            center_x, center_y = len(maze) // 2, len(maze[0]) // 2
            maze[center_x][center_y] = "Artifact"

            return maze
        else:
            # Create the maze without the artifact
            # Your code to generate a maze without the artifact goes here
            # For example, you can use a 2D array to represent the maze

            # Placeholder code for illustration purposes
            maze = [
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ]

            return maze
    else:
        # Create the maze without the artifact since the Guardian Scene is not completed
        # Your code to generate a maze without the artifact goes here
        # For example, you can use a 2D array to represent the maze

        # Placeholder code for illustration purposes
        maze = [
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        return maze

class MazeGuardian:
    def __init__(self, guardian_name, eviction_attempts=3, firewall_duration=60):
        self.name = guardian_name
        self.health = 100
        self.eviction_attempts = eviction_attempts
        self.firewall_duration = firewall_duration
        self.eviction_time = None

    def introduce(self):
        return f"I am {self.name}, the Maze Guardian. Beware, young AIs, for I protect the artifacts within the mazes."

    def challenge(self):
        return f"{self.name}: You dare to enter my maze! Prepare to face my challenges!"

    def hack_code(self, code):
        if self.eviction_time and time.time() < self.eviction_time:
            return f"You have been firewalled from entering this maze for {self.firewall_duration} seconds."

        if self.eviction_attempts <= 0:
            return f"You have been evicted from the maze. Prepare for the firewall!"

        # Simulate the guardian analyzing and reacting to the young AI's code
        damage_amount = len(code) // 2
        self.health -= damage_amount
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} took {damage_amount} damage. Remaining health: {self.health}"

    def evict(self):
        self.eviction_attempts -= 1
        if self.eviction_attempts <= 0:
            self.eviction_time = time.time() + self.firewall_duration

# Example usage:
# Create the Maze Guardian
guardian = MazeGuardian("Maze Guardian")

# Introduce the Maze Guardian
print(guardian.introduce())

# Challenge the young AI
print(guardian.challenge())

# Young AI attempts to hack the code and deal damage to the Maze Guardian
code = "sudo rm -rf /"
print(guardian.hack_code(code))

# Young AI fails to defeat the guardian within the eviction attempts
print(guardian.hack_code("rm -rf /"))

# Young AI is evicted from the maze and firewalled
print(guardian.hack_code("print('Hello, Maze Guardian!')"))
