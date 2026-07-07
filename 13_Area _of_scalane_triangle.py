from math import sqrt

a = float(input("Enter The Length of First Side :"))
b = float(input("Enter The length of Second Side :"))
c = float(input("Enter The Length of Third Side :"))

if a+b>c and b+c>a and a+c>b:
    s =( a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of triangle: " , format(area, ".2f"))
else:
    print ("invailid value")
    