import random

def tournament_selection(population, fitness_scores, tournament_size):
    """Selects two parents from the population using tournament selection."""
    # Turnuva için rastgele bireyler seç
    participants = random.sample(list(enumerate(population)), tournament_size)
    
    # Participants listesinden (index, chromosome) çiftleri olarak alınır
    # Fitness skorlarına göre sıralayarak en iyi iki bireyi bul
    sorted_participants = sorted(participants, key=lambda x: fitness_scores[x[0]], reverse=True)
    
    # En iyi iki bireyi dön
    return [population[idx] for idx, _ in sorted_participants[:2]]

