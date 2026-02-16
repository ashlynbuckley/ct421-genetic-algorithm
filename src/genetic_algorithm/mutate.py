# Written by Avalon Brathwaite
import random

def mutate(offspring, mutation_rate):
    mutated_offspring = []

    for timetable in offspring:
        timetable = [row[:] for row in timetable] # Avoid mutating original references

        if random.random() < mutation_rate:
            # Pick a random exam row within the timetable
            exam = random.randrange(len(timetable))
            slots = timetable[exam] # Gives us all the time slots for the random exam row chosen

            scheduled_exam_slot = slots.index(True)
            new_slot = random.randrange(len(slots))

           # Always pick a different slot
            while new_slot == scheduled_exam_slot:
                new_slot = random.randrange(len(slots))

            # Shift the current true exam slot to avoid violating constraints, this could give us consecutive exams or no exams scheduled at all.
            slots[scheduled_exam_slot] = False
            slots[new_slot] = True

            mutated_offspring.append(timetable)
        else:
            mutated_offspring.append(timetable)
    return mutated_offspring

# Visual Help timetable =
#     [False, True,  False],  # exam 0
#     [True,  False, False],  # exam 1
#     [False, False, True ],  # exam 2
#     [False, True,  False]   # exam 3
