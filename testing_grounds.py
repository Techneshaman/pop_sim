
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

my_tile = Tile()
my_tile.print_content()
