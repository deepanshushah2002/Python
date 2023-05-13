n = int(input("Enter a number:- "))
for i in range(n):
    for j in range(i):
        print(n - j, end=" ")
    for k in range(2*(n-i)-1):
        print(n - i, end=" ")
    for l in range(n-i+1,n+1):
        print(l, end=" ")
    print()
for i in range(1,n):
    for j in range(n-i-1):
        print(n-j, end=" ")
    for k in range(2*i+1):
        print(i+1, end=" ")
    for l in range(2+i,n+1):
        print(l, end=" ")
    print()
 