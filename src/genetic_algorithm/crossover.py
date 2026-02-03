# Written by Avalon Brathwaite

def crossover(population,results,selection_percentage):
    paired = []

   # Pair population with associated result
    for i in range(len(population)):
        paired.append((results[i],population[i]))

    # Sort the results based by fitness score
    paired.sort(reverse=True, key=lambda x: x[0]) # each x is the tuple score and population,
                                                  # so for each tuple get the fitness score (x[0]) and sort

    # Take the top % of parents
    num_parents = paired // selection_percentage
    parents = []
    for i in range(num_parents):
        parents.append(paired[i][1]) # Take only the timetable, not the fitness score

    # Preform crossover - Swap half of each parent with one another?

    return combinedTimetable