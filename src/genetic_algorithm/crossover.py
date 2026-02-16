# Written by Avalon Brathwaite
import numpy as np

def crossover(population):
    offspring = []

    # Preform Discrete crossover - Produces one child per crossover
    for i in range(0,len(population) -1, 2): # Steps of two so we don't reuse the same parent
        parent_one = population[i]
        parent_two = population[i+1]
        for _ in range(2):
            child = []
            for j in range(len(parent_one)): # We want children to be the same length as parents
                probability_of_crossover = np.random.uniform(low = 0, high = 1) # Random probability of child inheriting either parent one or twos genes
                if probability_of_crossover < 0.5 :
                    child.append(parent_one[j])
                else:
                    child.append(parent_two[j])

            # print("Parent One", parent_one)
            # print("Parent Two", parent_two)
            # print("Child", child)
            offspring.append(child)

    # print("Number of parents", len(population))
    # print("Offspring:", offspring, "\nOffspring Count:", len(offspring))
    return offspring