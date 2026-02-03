# Written by ashlyn do not touch EVERRRR ESPECIALLY AVALON
import sys

# Extracts variables from the file
def parse_variables(filename):
    with open(filename, "r") as f:
        variables = f.readline().split()
        n_exams = int(variables[0])
        n_slots = int(variables[1])
        n_students = int(variables[2])

    input_array = generate_input_array(filename, n_exams, n_students)
    return n_exams, n_slots, n_students, input_array

def generate_input_array(filename, n_exams, n_students):
    with open(filename, "r") as f:
        # For every student generate a new row with length = n_exams
        input_array = [[0 for _ in range(n_exams)] for _ in range(n_students)]
        # Skip the variables line
        next(f)
        for i, line in enumerate(f):
            j = 0
            for value in line:
                if not value.isspace():
                    if int(value) == 0:
                        input_array[i][j] = False
                    else:
                        input_array[i][j] = True
                    j+=1
    return input_array

# ENTRY POINT FUNCTION
def read_instance(filename):
    print("Reading input file...")
    n_exams, n_slots, n_students, input_array = parse_variables(filename)
    for row in input_array:
        print(*row)

# === STEPS ===
# read in file
hc_file = "tinyexample.txt"
# file_location = input("ENTER FILE PATHWAY:\n")
# print (file_location)
read_instance(hc_file)