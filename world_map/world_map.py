from world_map.tile import Tile

class WorldMap:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.citizens_to_spawn = 5
        self.food_per_cycle = 2
        self.board = []

    def generate_board(self):
        for y in range(self.height):
            next_row = []
            for x in range(self.width):
                next_row.append(Tile(x, y))
            self.board.append(next_row)

    def print_board(self):
        printable = ''
        for row in self.board:
            for tile in row:
                contents = tile.get_content()
                printable += contents
            printable += '\n'
