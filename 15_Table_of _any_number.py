def printtable(n):
    for i in range (1,11):
        print("%d * %d = %d" %(n,i,n*i))
a = int(input("Enter the number:"))
printtable(a)