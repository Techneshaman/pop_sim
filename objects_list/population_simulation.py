from objects_list.food import Food, NoFood
from objects_list.citizen import Citizen


class Tile:
    def __init__(self, x=0, y=0):
        self.contents = '0'
        self.x_coord = x
        self.y_coord = y

    def spawn_object(self, new_object):
        self.contents = new_object

    def destroy_object(self):
        self.contents = '0'

    def print_content(self):
        print(self.contents)

    def get_content(self):
        return self.contents


class WorldMap:
    def __init__(self):
        self.height = 5
        self.width = 5
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


class PopulationSimulation:
    def __init__(self):
        self.citizens_to_spawn = 5
        self.food_per_cycle = 2
        self.cycles_to_simulate = 5
        self.food_list = []
        self.pop_list = []
        self.spawn_world_map()
        self.spawn_initial_population()
        self.spawn_initial_food()

    def spawn_initial_population(self):
        self.pop_list = [Citizen() for i in range(self.citizens_to_spawn)]

    def spawn_initial_food(self):
        self.food_list = [Food() for i in range(self.food_per_cycle)]

    def spawn_world_map(self):
        self.world_map = WorldMap()
        self.world_map.generate_board()

    def get_food_item(self):
        if len(self.food_list) == 0:
            return NoFood()
        food_item = self.food_list.pop(0)
        return food_item

    def kill_the_dead(self):
        self.pop_list = [citizen for citizen in self.pop_list if citizen.is_alive]

    def generate_new_food(self):
        self.food_list = self.food_list + [Food() for i in range(self.food_per_cycle)]

    def tick(self):
        for citizen in self.pop_list:
            food_item = self.get_food_item()
            citizen.eat(food_item)
            citizen.survive_cycle()
        self.kill_the_dead()
        self.generate_new_food()
        self.cycles_to_simulate -= 1

    def get_debug_data(self):
        print('POPULATION OVERVIEW ON CYCLE %s' % self.cycles_to_simulate)
        for citizen in self.pop_list:
            print(citizen.get_pop_state())
        print('FOOD OVERVIEW ON CYCLE %s' % self.cycles_to_simulate)
        for food in self.food_list:
            print(food.get_food_state())
        print('BOARD:')
        self.world_map.print_board()
