a = int(input("Enter a Number"))
n = a
for i in range(n):
    print(" "*n, "*"*(2*i-1))
    n -= 1
n = a
for i in range(n):
    print(" "*i, "*"*(2*n-1))
    n -= 1
