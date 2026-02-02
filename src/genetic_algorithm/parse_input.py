# Written by ashlyn do not touch EVERRRR ESPECIALLY AVALON
import sys

# Extracts variables from the file
def parse_variables(filename):
    variables = []
    with open(filename, "r") as f:
        variable_line = f.readline()
        for char in variable_line:
            if not char.isspace():
                print("char: ", int(char))
                variables.append(int(char))
    # print(variables)
    n_exams = variables[0]
    n_slots = variables[1]
    n_students = variables[2]
    print(n_exams, n_slots, n_students)

# ENTRY POINT FUNCTION
def read_instance(filename):
    parse_variables(filename)

# === STEPS ===
# read in file
hc_file = "tinyexample.txt"
# file_location = input("ENTER FILE FATTY\n")
# print (file_location)
read_instance(hc_file)