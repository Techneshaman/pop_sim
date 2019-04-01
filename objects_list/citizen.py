class Citizen:
    def __init__(self):
        self.cycles_to_live = 15
        self.energy = 100
        self.food_per_cycle = 25
        self.is_alive = True
        self.breeding_cost = 50

    def survive_cycle(self):
        self.energy -= self.food_per_cycle
        self.cycles_to_live -= 1
        if self.cycles_to_live <= 0 or self.energy <= 0:
            self.is_alive = False

    def eat(self, food_object):
        self.energy += food_object.energetic_value

    def get_pop_state(self):
        return 'cycles_to_live: %s, energy: %s, food_per_cycle: %s, is_alive: %s' %(self.cycles_to_live,
                                                                                    self.energy,
                                                                                    self.food_per_cycle,
                                                                                    self.is_alive)
