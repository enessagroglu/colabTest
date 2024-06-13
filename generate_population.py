from tournament_selection import tournament_selection
from one_point_crossover import one_point_crossover
from fitness_function import fitness_function
from bit_mutation import bit_mutation

def generate_new_generation(streets_data, population, mutation_rate, tournament_size, coverage_radius, max_demand_per_station):
    """Generates a new generation using selection, crossover, and mutation."""
    fitness_scores = [fitness_function(chromosome, streets_data, coverage_radius, max_demand_per_station) for chromosome in population]
    new_population = []

    while len(new_population) < len(population):
        # Select two parents using tournament selection
        parents = tournament_selection(population, fitness_scores, tournament_size)
        # Perform one-point crossover to generate two children
        child1, child2 = one_point_crossover(parents[0], parents[1])
        # Apply mutation to each child
        child1 = bit_mutation(child1, mutation_rate)
        child2 = bit_mutation(child2, mutation_rate)
        # Add children to the new population
        new_population.extend([child1, child2])

    # Trim the new population to match the original size (in case it exceeded due to extend)
    return new_population[:len(population)]