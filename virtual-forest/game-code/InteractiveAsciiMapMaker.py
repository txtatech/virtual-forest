from asciimatics.screen import Screen

class InteractiveAsciiMapMaker:
    def __init__(self, map_data):
        self.map_data = [list(row) for row in map_data]
        self.player_x = 0
        self.player_y = 0
        self.find_player()

    def find_player(self):
        for y, row in enumerate(self.map_data):
            for x, char in enumerate(row):
                if char == '@':
                    self.player_x = x
                    self.player_y = y
                    return

    def move_player(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if (0 <= new_x < len(self.map_data[0]) and
            0 <= new_y < len(self.map_data) and
            self.map_data[new_y][new_x] != '#'):
            self.map_data[self.player_y][self.player_x] = ' '
            self.player_x = new_x
            self.player_y = new_y
            self.map_data[self.player_y][self.player_x] = '@'

    def create_map(self, screen):
        y_pos = screen.height // 2 - len(self.map_data) // 2
        x_pos = screen.width // 2 - len(self.map_data[0]) // 2

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

# Sample map data
sample_map_data = [
    "###################",
    "#                 #",
    "#       @         #",
    "#                 #",
    "###################",
]

# Create an instance of the class and run the map maker
if __name__ == "__main__":
    map_maker = InteractiveAsciiMapMaker(map_data=sample_map_data)
    Screen.wrapper(map_maker.main)
