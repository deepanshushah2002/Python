n=input("Enter a number")
m=int(n)
p=m
s=0
while m>0:
    r=m%10
    s=s+r**len(n)
    m=m//10
if (s==p):
    print("This is armstrong")
else:
    print("This is not armstrong")