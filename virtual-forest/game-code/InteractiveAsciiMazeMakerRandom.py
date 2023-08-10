from asciimatics.screen import Screen
import random

class InteractiveAsciiMazeMakerRandom:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_x = 1
        self.player_y = 1
        self.treasure_x = width // 2
        self.treasure_y = height // 2
        self.map_data = self.generate_maze()

    def generate_maze(self):
        maze = [['#' for _ in range(self.width)] for _ in range(self.height)]
        stack = [(self.player_x, self.player_y)]
        maze[self.player_y][self.player_x] = ' '

        while stack:
            x, y = stack[-1]
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            random.shuffle(neighbors)
            unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < self.width-1 and 0 < neighbor[1] < self.height-1 and maze[neighbor[1]][neighbor[0]] == '#']

            if unvisited_neighbors:
                nx, ny = unvisited_neighbors[0]
                maze[ny][nx] = ' '
                maze[(ny+y)//2][(nx+x)//2] = ' '
                stack.append((nx, ny))
            else:
                stack.pop()

        maze[self.player_y][self.player_x] = '@'
        maze[self.treasure_y][self.treasure_x] = '&'
        return maze

    def create_map(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                screen.print_at(self.map_data[y][x], x, y)

    def main(self, screen):
        while True:
            # Draw the map
            self.create_map(screen)
            screen.refresh()

            # Handle key inputs for movement
            key = screen.get_key()
            if key in (Screen.KEY_UP, ord('W')):
                if self.map_data[self.player_y - 1][self.player_x] == ' ':
                    self.map_data[self.player_y][self.player_x], self.map_data[self.player_y - 1][self.player_x] = ' ', '@'
                    self.player_y -= 1
            elif key in (Screen.KEY_DOWN, ord('S')):
                if self.map_data[self.player_y + 1][self.player_x] == ' ':
                    self.map_data[self.player_y][self.player_x], self.map_data[self.player_y + 1][self.player_x] = ' ', '@'
                    self.player_y += 1
            elif key in (Screen.KEY_LEFT, ord('A')):
                if self.map_data[self.player_y][self.player_x - 1] == ' ':
                    self.map_data[self.player_y][self.player_x], self.map_data[self.player_y][self.player_x - 1] = ' ', '@'
                    self.player_x -= 1
            elif key in (Screen.KEY_RIGHT, ord('D')):
                if self.map_data[self.player_y][self.player_x + 1] == ' ':
                    self.map_data[self.player_y][self.player_x], self.map_data[self.player_y][self.player_x + 1] = ' ', '@'
                    self.player_x += 1

# Create an instance of the class and run the map maker
if __name__ == "__main__":
    map_maker = InteractiveAsciiMazeMakerRandom(width=51, height=21)
    Screen.wrapper(map_maker.main)
