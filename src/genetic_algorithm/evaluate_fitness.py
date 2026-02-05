# Written by Karolina

def evaluate_population(population,input_array,n_timeslots):
    results=[]
    n_students = len(input_array)
    n_exams = len(input_array[0])
    # for every table in the generation
    for table in population:
        result = 100
        # for every student
        for i in range(n_students):
            schedule=[]
            # for every exam
            for j in range(n_exams):
                # if the student does the exam
                if input_array[i][j]:
                    # for every time slot
                    for k in range(n_timeslots):
                        # if the exam is at this time
                        if table[j][k]:
                            # append the time slot to the student's schedule
                            schedule.append(k)
            # prep for evaluation
            schedule = sorted(schedule)
            count=[0 for _ in range(n_timeslots)]
            consecutive = 0
            for l in range(len(schedule)):
                # soft constraints
                if l != 0:
                    if schedule[l] == (schedule[l-1]+1):
                        consecutive += 1
                    elif schedule[l] >= (schedule[l-1]+5):
                        result=result-5
                    elif schedule[l] != schedule[l-1]:
                        consecutive = 0
                if consecutive == 2:
                    result=result-5
                    consecutive = 0

                # hard constraint
                count[schedule[l]] += 1
                if count[schedule[l]] > 1:
                    result=result-10
        results.append(result)
    return results

