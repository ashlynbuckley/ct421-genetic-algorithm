# Written by Karolina

def evaluate_population(population,input_array):
    results=[]
    for table in population:
        result = 100
        for i in range(len(input_array)):
            schedule=[]
            for j in range(len(input_array[0])):
                if input_array[i][j]:
                    for k in range(len(table[0])):
                        if table[j][k]:
                            schedule.append(k)
                            print(schedule)
            count=[0 for _ in range(len(table[0]))]
            consecutive = 0
            for l in range(len(schedule)):
                if l != 0 and (schedule[l] == schedule[l-1]+1 or schedule[l] == schedule[l-1]-1):
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive == 2:
                    result=result-5
                    consecutive = 0
                count[schedule[l]] += 1
                if count[schedule[l]] > 1:
                    result=result-10
        results.append(result)
    return results

