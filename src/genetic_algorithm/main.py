# Written by Karolina
import init_population as init_pop
from evaluate_fitness import evaluate_population
from crossover import crossover
from mutate import mutate
from src.genetic_algorithm.parse_input import read_input_file
from src.genetic_algorithm.selection import selection_process

# Fields
input_file = "tinyexample.txt"
population_size = 1000
elite_percentage = 0.05
t_size = 5
mutation_rate = 1
generations = 500

# Parse input
n_exams, n_slots, n_students, input_array = read_input_file(input_file)

# Initialise populations
population = init_pop.init_population(population_size, n_exams, n_slots)
print(population)

for i in range(generations):
    # Fitness
    results = evaluate_population(population, input_array, n_slots)
    # print(results)

    # Select chromosomes to continue with
    next_generation = selection_process(population, results, elite_percentage, t_size)

    # Crossover & Mutate
    # Avalon Brathwaite
    offspring = crossover(next_generation)
    mutated_offspring = mutate(offspring, mutation_rate)

    population = mutated_offspring
    print("population after", i, "loop", population)

print("Final timetables: ",population)
