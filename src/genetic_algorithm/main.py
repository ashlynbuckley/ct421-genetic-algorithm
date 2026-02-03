# Written by Karolina
import init_population as init_pop
import parse_input as pi
from evaluate_fitness import evaluate_population
from src.genetic_algorithm.crossover import crossover

input_file = "tinyexample.txt"
population_size = 100
selection_percentage = 0.2
n_exams, n_slots, n_students, input_array = pi.parse_variables(input_file)
population = init_pop.init_population(population_size, n_exams, n_slots)
print(population)
results = evaluate_population(population, input_array)
print(results)
crossover(population, results)
print(crossover(population, results, selection_percentage))