import random

def one_point_crossover(parent1, parent2):
    """Performs one-point crossover on two parent chromosomes, using Python lists."""
    if len(parent1) != len(parent2):
        raise ValueError("Parent chromosomes must be of equal length.")

    # Randomly select a crossover point between 1 and length of the chromosome - 1
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Create children by combining the genes from parents at the crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2