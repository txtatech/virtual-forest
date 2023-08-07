class Player:
    def __init__(self, name):
        self.name = name

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = []

class Exit:
    def __init__(self, direction, destination):
        self.direction = direction
        self.destination = destination

class MUDGame:
    def __init__(self):
        self.rooms = []
        self.players = []
        self.currentPlayer = None
        self.currentRoom = None

    def init_rooms(self):
        # Replace this with your own logic to create rooms and set up the game world
        room1 = Room("Room 1", "This is room 1")
        room2 = Room("Room 2", "This is room 2")
        exit1 = Exit("north", room2)
        room1.exits = [exit1]
        self.rooms = [room1, room2]

    def move_player(self, destRoom):
        if destRoom == self.currentRoom:
            print("You are already in this room.")
        else:
            self.currentRoom = destRoom
            print("You have moved to " + destRoom.name)

    def handle_command(self, command):
        if command == "look":
            print(self.currentRoom.description)
        elif command == "north":
            exit_direction = "north"
            exit = self.find_exit(exit_direction, self.currentRoom.exits)
            if exit is None:
                print("There is no exit in that direction.")
            else:
                self.move_player(exit.destination)
        else:
            print("Invalid command.")

    def find_exit(self, direction, exits):
        for exit in exits:
            if exit.direction == direction:
                return exit
        return None

    def game_loop(self):
        while True:
            command = input()
            self.handle_command(command)

def main():
    game = MUDGame()
    game.init_rooms()

    player = Player("Player")
    game.players.append(player)
    game.currentPlayer = player
    game.currentRoom = game.rooms[0]  # Start the player in the first room

    game.game_loop()

# Start the game by invoking the main function
main()
