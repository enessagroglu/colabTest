def read_fitness_file(file_path):
    generations = []
    fitness_values = []

    with open(file_path, 'r') as file:
        for line in file:
            try:
                generation, fitness = line.strip().split(':')
                generations.append(int(generation))
                fitness_values.append(float(fitness))
            except ValueError:
                print(f"Line skipped due to format error: {line}")

    return generations, fitness_values

def calculate_best_and_average_fitness(generations, fitness_values):
    best_fitness = max(fitness_values)
    best_generation = generations[fitness_values.index(best_fitness)]
    average_fitness = sum(fitness_values) / len(fitness_values)
    return best_fitness, best_generation, average_fitness

def main():
    file_path = 'best_fitness_per_generation.txt'
    generations, fitness_values = read_fitness_file(file_path)

    if not fitness_values:
        print("No valid fitness values found.")
        return

    best_fitness, best_generation, average_fitness = calculate_best_and_average_fitness(generations, fitness_values)

    print(f"Best Fitness Value: {best_fitness} (Generation: {best_generation})")
    print(f"Average Fitness Value: {average_fitness}")

if __name__ == "__main__":
    main()
