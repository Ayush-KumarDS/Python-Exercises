def sum_of_digits(n):
    sum = 0 
    while n>0:
        rem = n%10
        sum += rem
        n = n//10
    return sum
a = int(input("Enter Any Number : "))
print("Sum of digits are : ",sum_of_digits(a))

