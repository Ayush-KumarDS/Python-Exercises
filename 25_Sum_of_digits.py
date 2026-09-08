def DigitSum(n):
    if n <0:
        return "Invalid Input....Please try again."
    if n == 0:
        return 0
    else:
        return n%10 + DigitSum(n//10)
b = int(input("Enter Any Number : "))
print(DigitSum(b))