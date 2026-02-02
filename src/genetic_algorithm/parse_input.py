# Written by ashlyn do not touch EVERRRR ESPECIALLY AVALON
import sys

# Extracts variables from the file
def parse_variables(filename):
    variables = []
    with open(filename, "r") as f:
        variable_line = f.readline()
        for char in variable_line:
            if not char.isspace():
                variables.append(int(char))
    n_exams = variables[0]
    n_slots = variables[1]
    n_students = variables[2]
    generate_input_array(filename, n_exams, n_students)

def generate_input_array(filename, n_exams, n_students):
    with open(filename, "r") as f:
        # For every student generate a new row with length = n_exams
        input_matrix = [[0 for _ in range(n_exams)] for _ in range(n_students)]
        # Skip the variables line
        next(f)
        for i, line in enumerate(f):
            j = 0
            for value in line:
                if not value.isspace():
                    if int(value) == 0:
                        input_matrix[i][j] = False
                    else:
                        input_matrix[i][j] = True
                    j+=1
    for row in input_matrix:
        print(*row)


# ENTRY POINT FUNCTION
def read_instance(filename):
    parse_variables(filename)
#     NEXT: CREATE ARRAYS

# === STEPS ===
# read in file
hc_file = "tinyexample.txt"
# file_location = input("ENTER FILE FATTY\n")
# print (file_location)
read_instance(hc_file)