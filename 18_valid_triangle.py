def valid_triangle(a,b,c):
    if (a+b <=c)or(b+c<=a)or(c+a<=b):
        return False
    else:
        return True
q = int(input("Enter the 1st length of tringle :"))
r = int(input("Enter the 2nd length of tringle :"))
w = int(input("Enter the 3rd length of tringle :"))
if valid_triangle(q,r,w):
    print("valid")
else:
    print("Invalid")
    