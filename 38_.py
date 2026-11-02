def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)
print(map_longest(['python89888', 'django', 'sql', 'html', 'css']))