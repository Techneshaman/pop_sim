from world_map.tile import Tile
from random import randint


class WorldMap(object):
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
        print(printable)

    def place_citizen(self, citizen_name):
        print('placing citizen')
        random_height = randint(0, self.height - 1)
        random_width = randint(0, self.width - 1)
        my_tile = self.board[random_height][random_width]
        print('my tile before: {}'.format(my_tile.get_content()))
        my_tile.spawn_object(citizen_name)
        print('my tile after: {}'.format(my_tile.get_content()))
        self.board[random_height][random_width] = my_tile
