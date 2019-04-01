from objects_list.population_simulation import PopulationSimulation


my_sim = PopulationSimulation()

for i in range(5):
    my_sim.tick()
    my_sim.get_debug_data()
