n=int(input("Enter a Number"))
for i in range(n):
    print(" "*n,"*"*(2*i-1))
    #print("*"*(2*i-1))
    n -=1
    #print('*'*i,end="")
    #print("*"*(i-1),end="")