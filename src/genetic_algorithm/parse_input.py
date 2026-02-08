# Written by Ashlyn

# Extracts variables from the file
def parse_variables(filename):
    with open(filename, "r") as f:
        # Look at the first line, turn it into a list of str
        variables = f.readline().split()
        # Grab each and use int() to convert them from str -> int
        n_exams = int(variables[0])
        n_slots = int(variables[1])
        n_students = int(variables[2])
    return n_exams, n_slots, n_students

# Using variables extracted, generate a boolean 2d list of the txt file data
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
def read_input_file(filename):
    print("Reading input file...")
    n_exams, n_slots, n_students = parse_variables(filename)
    input_array = generate_input_array(filename, n_exams, n_students)
    # For debugging
    for row in input_array:
        print(*row)
    return n_exams, n_slots, n_students, input_array