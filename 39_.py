def filter(words):
    result = []
    for word in words:
        if len(word) >=4:
            result.append(word)
    return result
print(filter(['python', 'django', 'sql', 'html', 'css']))