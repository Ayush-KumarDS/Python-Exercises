def count_str(items):
    total = 0
    
    for item in items:
        if type(item) == str: # if isinstance(item, str):
            total += 1
    return total

print(count_str(['python', 'django', 'sql', 'html', 'css', 1, 2, 3, 4, 5]))