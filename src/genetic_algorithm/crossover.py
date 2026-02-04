# Written by Avalon Brathwaite
import numpy as np

def crossover(population,results,selection_percentage):
    paired = []
    offspring = []

######################################################################################################

   # Pair population with associated result
    for i in range(len(population)):
        paired.append((results[i],population[i]))

    # Sort the results based by fitness score
    paired.sort(reverse=True, key=lambda x: x[0]) # each x is the tuple score and population,
                                                  # so for each tuple get the fitness score (x[0]) and sort

    # Take the top % of parents
    num_parents = int(len(paired) * selection_percentage)
    parents = []
    for i in range(num_parents):
        parents.append(paired[i][1]) # Take only the timetable, not the fitness score

######################################################################################################

    # Preform Discrete crossover - Produces one child per crossover
    for i in range(0,len(parents) -1, 2): # Steps of two so we don't reuse the same parent
        parent_one = parents[i]
        parent_two = parents[i+1]
        child = []
        for j in range(len(parent_one)): # We want children to be the same length as parents
            probability_of_crossover = np.random.uniform(low = 0, high = 1) # Random probability of child inheriting either parent one or twos genes
            if probability_of_crossover < 0.5 :
                child.append(parent_one[j])
            else:
                child.append(parent_two[j])

        print("Parent One", parent_one)
        print("Parent Two", parent_two)
        print("Child", child)
        offspring.append(child)

    print("Number of parents", len(parents))
    print("Offspring:", offspring, "\nOffspring Count:", len(offspring))
    return offspring