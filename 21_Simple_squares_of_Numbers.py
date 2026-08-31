# create a list of squares

def Square_numbers(n):
    square = [i**2 for i in range (1,n)]
    return square
print("The squares of numbers are :", Square_numbers(15))

# fillter even numbers
def Square_numbers_1(n):
    Even_square = [i**2 for i in range (1,n) if i%2==0]
    return Even_square
print("The sqaure of numbers : ", Square_numbers_1(8))

def Square_numbers_2(n):
    Even_square = [i**2 for i in range (1,n) if i%2!=0]
    return Even_square
print("The sqaure of numbers : ", Square_numbers_2(8))