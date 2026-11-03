def filter_count_str(items):
    total = 0
    for item in items:
        if isinstance(item,str):
            if len(item) >= 4:
                total += 1
    return total

print(filter_count_str(['python', 'django', 'sql', 'html', 'css', 1, 2, 3, 4, 5]))