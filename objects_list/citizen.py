class Citizen(object):
    def __init__(self, citizen_name):
        self.cycles_to_live = 15
        self.energy = 100
        self.food_per_cycle = 25
        self.is_alive = True
        self.breeding_cost = 50
        self.citizen_name = citizen_name

    def survive_cycle(self):
        self.energy -= self.food_per_cycle
        self.cycles_to_live -= 1
        if self.cycles_to_live <= 0 or self.energy <= 0:
            self.is_alive = False

    def eat(self, food_object):
        self.energy += food_object.energetic_value

    def get_name(self):
        return self.citizen_name

    def get_pop_state(self):
        return 'cycles_to_live: %s, energy: %s, food_per_cycle: %s, is_alive: %s, name: %s'\
               % (self.cycles_to_live,
                  self.energy,
                  self.food_per_cycle,
                  self.is_alive,
                  self.citizen_name)
