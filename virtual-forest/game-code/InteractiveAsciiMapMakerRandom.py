import random
from asciimatics.screen import Screen

class InteractiveAsciiMapMakerRandom:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_x = random.randint(1, width - 2)
        self.player_y = random.randint(1, height - 2)
        self.map_data = self.generate_map()

    def generate_map(self):
        map_data = [['#' for _ in range(self.width)] for _ in range(self.height)]
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if random.random() < 0.7:
                    map_data[y][x] = ' '
        map_data[self.player_y][self.player_x] = '@'
        return map_data

    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if self.map_data[new_y][new_x] == ' ':
            self.map_data[self.player_y][self.player_x] = ' '
            self.player_x = new_x
            self.player_y = new_y
            self.map_data[self.player_y][self.player_x] = '@'

    def create_map(self, screen):
        y_pos = 0
        x_pos = 0

        for y, line in enumerate(self.map_data):
            screen.print_at(''.join(line), x_pos, y_pos + y)

        screen.refresh()

    def main(self, screen):
        try:
            while True:
                self.create_map(screen)
                event = screen.get_key()
                if event == Screen.KEY_UP:
                    self.move_player(0, -1)
                elif event == Screen.KEY_DOWN:
                    self.move_player(0, 1)
                elif event == Screen.KEY_LEFT:
                    self.move_player(-1, 0)
                elif event == Screen.KEY_RIGHT:
                    self.move_player(1, 0)
                elif event == ord('q'):
                    return
        except Exception as e:
            print(e)

# Create an instance of the class and run the map maker
if __name__ == "__main__":
    map_maker = InteractiveAsciiMapMakerRandom(width=50, height=20)
    Screen.wrapper(map_maker.main)
