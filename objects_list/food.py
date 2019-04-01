class Food:
    def __init__(self):
        self.energetic_value = 10

    def get_food_state(self):
        return 'energetic_value: %s' % self.energetic_value


class NoFood(Food):
    def __init__(self):
        self.energetic_value = 0
