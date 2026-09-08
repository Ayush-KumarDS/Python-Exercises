def prime(n):
    if n <= 1:
        return "Invalid Input....Please try again."
    for i in range(2, int(n**0.5) ):
        if n % i == 0:
            return "Not a Prime Number"
            break
    return "It is a Prime Number"
b = int(input("Enter Any Number : "))
print(prime(b))