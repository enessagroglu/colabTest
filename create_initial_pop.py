import json
import numpy as np

def read_street_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        streets_data = json.load(file)
    return streets_data

def calculate_weights(streets_data):
    population_rates = np.array([street["rate_of_population"] for street in streets_data])
    demands = np.array([street["demand"] for street in streets_data])
    norm_population_rates = population_rates / np.max(population_rates)
    norm_demands = demands / np.max(demands)
    weights = 0.3 * norm_population_rates + 0.7 * norm_demands
    return weights

def create_initial_population(weights, population_size, num_streets):
    return np.random.binomial(1, weights, (population_size, num_streets))

def write_population_to_json(chromosomes, output_path):
    output_data = {"chromosomes": chromosomes.tolist()}
    with open(output_path, 'w') as outfile:
        json.dump(output_data, outfile)

def generate_initial_population(filepath, output_path):
    streets_data = read_street_data(filepath)
    weights = calculate_weights(streets_data)
    population_size = 100
    num_streets = len(streets_data)
    chromosomes = create_initial_population(weights, population_size, num_streets)
    write_population_to_json(chromosomes, output_path)

def create_first_population():
    #basibuyuk
    basibuyuk_path = r"/content/colabTest/data/basibuyuk.json"
    basibuyuk_output_path = r"/content/colabTest/data/basibuyuk_initial_population.json"
    generate_initial_population(basibuyuk_path, basibuyuk_output_path)

    #tepeustu
    tepeustu_path = r"/content/colabTest/data/tepeustu.json"
    tepeustu_output_path = r"/content/colabTest/data/tepeustu_initial_population.json"
    generate_initial_population(tepeustu_path, tepeustu_output_path)

    #resadiye
    resadiye_path = r"/content/colabTest/data/resadiye.json"
    resadiye_output_path = r"/content/colabTest/data/resadiye_initial_population.json"
    generate_initial_population(resadiye_path, resadiye_output_path)
