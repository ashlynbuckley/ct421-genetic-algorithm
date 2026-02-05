# Written by Avalon Brathwaite
from random import random


def mutate(offspring):
    mutated_offspring = []

    for i in range(offspring):
        # Change random value in all offspring to introduce randomness
        random_bool = random.randint(0, 1)
        rand_index = random.randint(len(offspring))
        offspring[rand_index] = random_bool
    return mutated_offspring