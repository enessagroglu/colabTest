from math import radians, cos, sin, asin, sqrt

from math import sqrt

def euclidean_distance_km(lon1, lat1, lon2, lat2):
    # Calculate Euclidean distance between coordinates
    # Assuming each degree is approximately 111 kilometers at the equator
    dist = sqrt((lon2 - lon1)**2 + (lat2 - lat1)**2)
    return dist * 111


def fitness_function(chromosome, streets_data, coverage_radius, max_demand_per_station):
    total_demand = sum(street['demand'] for street in streets_data)
    covered_demand = 0
    total_stations = sum(chromosome)
    penalty = 0

    for i, active in enumerate(chromosome):
        if active:
            station_coord = (streets_data[i]['longitude'], streets_data[i]['latitude'])
            local_covered_demand = 0

            for street in streets_data:
                street_coord = (street['longitude'], street['latitude'])
                distance = euclidean_distance_km(float(station_coord[0]), float(station_coord[1]), float(street_coord[0]), float(street_coord[1]))

                if distance <= coverage_radius:
                    local_covered_demand += street['demand']
                    if local_covered_demand > max_demand_per_station:
                        break

            covered_demand += min(local_covered_demand, max_demand_per_station)

    covered_demand_ratio = covered_demand / total_demand
    penalty = (total_demand - covered_demand) * 0.01 + total_stations * 0.05  
    fitness = covered_demand_ratio - penalty

    return fitness

