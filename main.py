from fitness_function import fitness_function
from generate_population import generate_new_generation
import json
from create_initial_pop import create_first_population

def genetic_algorithm(streets_data, population, max_generations, max_stagnant_generations, mutation_rate, tournament_size, coverage_radius, max_demand_per_station):
    best_fitness = -float('inf')
    stagnant_generations = 0

    with open("best_fitness_per_generation.txt", "w") as file:
        for generation in range(max_generations):
            # Fitness hesapla ve yeni nesli oluştur
            fitness_scores = [fitness_function(chromosome, streets_data, coverage_radius, max_demand_per_station) for chromosome in population]
            
            # En iyi fitness değerini güncelle
            best_generation_fitness = max(fitness_scores)
            if best_generation_fitness > best_fitness:
                best_fitness = best_generation_fitness
                stagnant_generations = 0
            else:
                stagnant_generations += 1
            
            # Dosyaya en iyi fitness değerini yaz
            file.write(f"{generation + 1}:{best_fitness}\n")
            
            # Durma koşulları
            if stagnant_generations >= max_stagnant_generations:
                print(f"No improvement for {max_stagnant_generations} generations, stopping early at generation {generation}")
                break
            
            # Popülasyonu yeni nesil ile değiştir
            new_population = generate_new_generation(streets_data, population, mutation_rate, tournament_size, coverage_radius, max_demand_per_station)
            population = new_population

    return population, best_fitness

def read_street_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        streets_data = json.load(file)
    return streets_data

def save_best_solution_to_json(chromosome, filepath='best_solution.json'):
    """Saves the best solution chromosome to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump({'best_chromosome': chromosome}, file, ensure_ascii=False, indent=4)

def read_population_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['chromosomes']

def map_and_save_streets_with_status(streets_data, best_chromosome, output_filepath='streets_with_bs_status.json'):
    """Maps streets to chromosome values indicating whether a base station is placed or not, and saves to a JSON file including coordinates."""
    # Create a list of dictionaries where each street is mapped to the corresponding chromosome value along with longitude and latitude
    streets_with_status = [
        {
            "street_name": street["name"],
            "latitude": street["latitude"],
            "longitude": street["longitude"],
            "has_base_station": bool(best_chromosome[i])  # True if 1, False if 0
        }
        for i, street in enumerate(streets_data)
    ]

    # Save this data to a JSON file
    with open(output_filepath, 'w', encoding='utf-8') as file:
        json.dump({'streets_with_bs_status': streets_with_status}, file, ensure_ascii=False, indent=4)

    print(f"Street status data has been saved to {output_filepath}")

def calculate_cost_from_best_solution(base_station_cost, filepath):
    """
    Calculate the total cost based on the best solution JSON file.
    
    Args:
        filepath (str): Path to the best solution JSON file.
        base_station_cost (int): Cost per base station.
    
    Returns:
        int: Total cost of all placed base stations.
    """
    try:
        # Read the best solution JSON file
        with open(filepath, 'r', encoding='utf-8') as file:
            best_solution = json.load(file)
        
        # Get the chromosome representing the best solution
        chromosome = best_solution['best_chromosome']
        
        # Count the number of 1s in the chromosome
        num_base_stations = sum(chromosome)
        
        # Calculate the total cost
        total_cost = num_base_stations * base_station_cost 
        
        return total_cost
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing best solution file: {e}")
        return None

def simulation(choice, max_generations=10000, max_stagnant_generations=10000, mutation_rate=0.196, tournament_size=4, coverage_radius=5, max_demand_per_station=100):
    
    # paths for street data and initial population JSON files
    if choice == 1:
        streets_filepath = r"/content/colabTest/data/basibuyuk.json"
        population_filepath = r"/content/colabTest/data/basibuyuk_initial_population.json"
    elif choice == 2:
        streets_filepath = r"/content/colabTest/data/resadiye.json"
        population_filepath = r"/content/colabTest/data/resadiye_initial_population.json"
    elif choice == 3:
        streets_filepath = r"/content/colabTest/data/tepeustu.json"
        population_filepath = r"/content/colabTest/data/tepeustu_initial_population.json"
    
    create_first_population()
    
    # Read street data and initial population
    streets_data = read_street_data(streets_filepath)
    population = read_population_from_json(population_filepath)

    # Run the genetic algorithm
    final_population, best_fitness = genetic_algorithm(streets_data, population, max_generations, max_stagnant_generations, mutation_rate, tournament_size, coverage_radius, max_demand_per_station)

    # Find the best chromosome from the final population
    best_chromosome = max(final_population, key=lambda x: fitness_function(x, streets_data, coverage_radius, max_demand_per_station))

    # Save the best chromosome to a JSON file
    save_best_solution_to_json(best_chromosome)

    # Map streets with their base station status (0 or 1) and save to a JSON file
    map_and_save_streets_with_status(streets_data, best_chromosome)

    total_cost = calculate_cost_from_best_solution(100, 'best_solution.json')
    num_base_stations = sum(best_chromosome)

    # Print the best fitness and total cost achieved
    print("Best Fitness Achieved:", best_fitness)
    print("Total Cost of Best Solution:", total_cost)
    print("Number of Base Stations:", num_base_stations)
    print("Total Demand:", sum(street['demand'] for street in streets_data))

def menu():
    print(
        """
        Select a map:
        [1] Basibuyuk
        [2] Resadiye
        [3] Tepeustu
        [4] Exit
    """
    )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        simulation(choice)
    elif choice == 2:
        simulation(choice)
    elif choice == 3:
        simulation(choice)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()

def main():
    menu()

if __name__ == "__main__":
    main()
