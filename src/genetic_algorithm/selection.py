# Written by Ashlyn and Avalon ❀⸜(˶´ ˘ `˶)⸝❀
import random

def generate_new_generation(parents, elites):
    next_generation = parents + elites
    return next_generation

# Survival of the fittest logic (in random subsets to vary what passes on)
def tournament_selection(paired, n_parents, t_size):
    selected = 0
    parents = []
    while selected != n_parents:
        contenders = []
        # Select contenders randomly (with replacement)
        for _ in range(t_size):
            rand_chromosome = paired[random.randint(0, len(paired) - 1)]
            contenders.append(rand_chromosome)
        # FIGHT!
        contenders.sort(reverse=True, key=lambda x: x[0])
        parents.append(contenders[0])
        selected += 1
    return parents

# Pick the best individuals of the gen and ensure they carry into the next
def select_elites(paired, elite_percentage):
    # Select top % (number may vary)
    n_elites = int(elite_percentage * len(paired))
    # Append them to a separate list
    elites = []
    for _ in range(n_elites):
        # Append the timetables of the elite solutions, remove them from the main pool
        elites.append(paired.pop(0))
    return elites

def pair_results_chromosomes(population, results):
    paired = []
    # Create tuples of population with associated result
    for i in range(len(population)):
        paired.append((results[i], population[i]))
    # Sort descending
    paired.sort(reverse=True, key=lambda x: x[0])
    return paired

def selection_process(population, results, elite_percentage, t_size):
    paired = pair_results_chromosomes(population, results)
    elites = select_elites(paired, elite_percentage)
    n_parents = len(paired)
    selected = tournament_selection(paired, n_parents, t_size)
    next_generation = generate_new_generation(selected, elites)
