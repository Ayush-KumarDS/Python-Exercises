def fact(n):
    result = 1
    i = 2
    while i<=n:
        result *=i
        i+=1
    return result
a = int(input("enter any number"))
print("Factorial of given number is : ", fact(a))