# Written by Karolina
from random import randrange

def init_population(population_size,n,k):
    population = []
    for i in range(population_size):
        timetable = [[False for _ in range(k)] for _ in range(n)]
        for j in range(n):
            r = randrange(k)
            timetable[j][r]=True
        population.append(timetable)
    return population