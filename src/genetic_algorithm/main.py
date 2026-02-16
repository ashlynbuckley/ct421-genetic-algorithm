import numpy as np
import plt

import init_population as init_pop
from evaluate_fitness import evaluate_population
from crossover import crossover
from mutate import mutate
from src.genetic_algorithm.parse_input import read_input_file
from src.genetic_algorithm.selection import selection_process

# Fields
input_file = "test_case1.txt"
population_size = 100
elite_percentage = 0.05
t_size = 5
mutation_rate = 0.3
generations = 500
multiple_run_mean = []
multiple_run_max = []
multiple_run_min = []
multiple_run_std = []
multiple_run_count = 100

# Parse input
n_exams, n_slots, n_students, input_array = read_input_file(input_file)

for x in range(multiple_run_count):
    # Initialise populations
    population = init_pop.init_population(population_size, n_exams, n_slots)
    print(population)

    mean_results = []
    max_results = []
    min_results = []
    std_results = []
    for i in range(generations):
        # Fitness
        results = evaluate_population(population, input_array, n_slots)
        mean_results.append(np.mean(results))
        max_results.append(np.max(results))
        min_results.append(np.min(results))
        std_results.append(np.std(results))

        # print(results)

        # Select chromosomes to continue with
        next_generation = selection_process(population, results, elite_percentage, t_size)

        # Crossover & Mutate
        offspring = crossover(next_generation)
        mutated_offspring = mutate(offspring, mutation_rate)

        population = mutated_offspring
        print("population after", i, "loop", population)

    # print("Final timetables: ",population)

    # Avalon Brathwaite
    # Evaluate final population
    final_results = evaluate_population(population, input_array, n_slots)
    multiple_run_mean.append(np.mean(mean_results))
    multiple_run_max.append(np.max(final_results))
    multiple_run_min.append(np.min(final_results))
    multiple_run_std.append(np.std(final_results))

    # Get best timetable
    best_index = max(range(len(final_results)), key=lambda i: final_results[i])
    best_fitness = final_results[best_index]
    best_timetable = population[best_index]

    print("\nPerformance Results:")
    print("Best fitness achieved:", best_fitness)
    for row in best_timetable:
        print(*row)

    #plot gen graph
    plt.plot(mean_results)
    plt.title('Fitness over generations')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.show()

#plot run graph
plt.plot(multiple_run_mean, color='r', label='mean')
plt.plot(multiple_run_max, color='b', label='max')
plt.plot(multiple_run_min, color='g', label='min')
plt.plot(multiple_run_std, color='k', label='std')
plt.title('Fitness over runs')
plt.xlabel('Runs')
plt.ylabel('Fitness')
plt.legend()
plt.show()