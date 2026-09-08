techs = ('python', 'java', 'sql', 'aws')

# Convert tuple to list (since tuples are immutable)
techs_list = list(techs)

# Selection sort
n = len(techs_list)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if techs_list[j] < techs_list[min_index]:
            min_index = j
    # Swap the found minimum with the first element
    techs_list[i], techs_list[min_index] = techs_list[min_index], techs_list[i]

# Convert back to tuple
techs = tuple(techs_list)
print(techs)
