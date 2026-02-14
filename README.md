# CT421 Assignment 1: Genetic Algorithm

### Ashlyn Buckley (22440672), Avalon Brathwaite (22400924), Karolina Fijalkowska (22404136)

---
### Code Structure

main.py details the workflow of the algorithm:

Firstly, read_input_files(), found in parse_input.py, extracts n_exams, n_slots, n_students and input_array.

Then, these are used to initialise a population using init_population(), found in init_population.py. Population is stored in a list.

We then loop over every generation and do the following tasks:

- evaluate fitness
- select parents for next generation
- crossover
- mutate

and so on...

Evaluating fitness includes using the evaluate_population() function from evaluate_fitness.py. This returns the results for each chromosome in a list.

The selection_process() function takes in the population, the results, the elite percentage and the tournament size to produce the selected parents for a new generation. It returns them in a list.

Crossover() (from crossover.py) uses the next_generation list to crossover and produce offspring, which are returned in a list.

That list is taken and used by mutate() (from mutate.py) to mutate them. It returns the mutated population for that generation.

That generation is then either evaluated or is the final generation of the algorithm and the loop is completed.

