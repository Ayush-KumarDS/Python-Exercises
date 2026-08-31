def fact(n):
    result = 1
    i=2
    while i<=n:
        result = result*i
        i+=1
    return result
def npr(n,r):
    return fact(n)//fact(n-r)
a = int(input("Enter the value of n :"))
b = int(input("Enter the value of r :"))
print("The Permutation of given number is : ", npr(a,b))

# def fact (n):
#     result=1
#     for i in range (2,n+1):
#         result*=i
#     return result
# print("result = " , fact(5))