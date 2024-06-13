import json
import random

# Talep oranları sabit kalacak
demand_ratios = [0.3, 0.5, 0.1]

# Mahalle dosya isimleri ve nüfusları
neighborhood_files = ["data/basibuyuk.json", "data/resadiye.json", "data/tepeustu.json"]
neighborhood_populations_file = "data/neighborhood_pop.json"

# Her mahalle için nüfus bilgilerini yükle
with open(neighborhood_populations_file, "r", encoding="utf-8") as pop_file:
    neighborhood_populations = json.load(pop_file)["neighborhood_populations"]

for neighborhood_file in neighborhood_files:
    with open(neighborhood_file, "r", encoding="utf-8") as street_file:
        streets = json.load(street_file)

    # Toplam rate değerlerini hesaplama
    total_rates = sum(street["rate_of_population"] for street in streets)

    # Sokaklara talep değerleri ve nüfus dağıtma
    for street in streets:
        rate = street["rate_of_population"]

        # Nüfus dağıtma
        street["population"] = int((rate / total_rates) * neighborhood_populations[neighborhood_file.split("/")[1].split(".")[0].lower()])

        # Talep hesaplama
        population = street["population"]
        if population > 0:
            demand_ratio = random.choice(demand_ratios)
            demand = int(population * demand_ratio)
        else:
            demand = 0
        street["demand"] = demand

    # Güncellenmiş verileri kendi dosyasına yazma
    with open(neighborhood_file, "w", encoding="utf-8") as street_file:
        json.dump(streets, street_file, indent=4, ensure_ascii=False)