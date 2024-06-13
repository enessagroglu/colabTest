import numpy as np

def bit_mutation(chromosome, mutation_rate):
    """Applies bit mutation to a chromosome with a given mutation rate."""
    for i in range(len(chromosome)):
        if np.random.rand() < mutation_rate:
            # Flip the bit: if 1 change to 0, if 0 change to 1
            chromosome[i] = 1 - chromosome[i]
    return chromosome