def reverse_number(n):
    rev = 0
    while n>0:
        r = n%10
        rev = rev*10 + r
        n = n//10
    return rev
a = int(input("enter any number:"))
print("Given number is reversed :",reverse_number(a) )