techs = ('python', 'java', 'sql', 'aws')

# Convert tuple to list for sorting
techs_list = list(techs)

# Bubble sort
n = len(techs_list)
for i in range(n):
    for j in range(0, n-i-1):
        if techs_list[j] > techs_list[j+1]:
            # Swap
            techs_list[j], techs_list[j+1] = techs_list[j+1], techs_list[j]

# Convert back to tuple
techs = tuple(techs_list)
print(techs)
