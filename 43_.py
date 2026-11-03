def duplicates_remover(items):
    result= []
    for item in items:
        if item not in result:
            result.append(item)
    return result
nums = [1,1,2,5,6,8,2,4,3,9,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

print(duplicates_remover(nums))