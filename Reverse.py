x=int(input("Enter a 3 digit a number"))
a=x%10
x//=10
b=x%10
x//=10
c=x%10
x//=10
print("The reverse of the given number is",a*100+b*10+c*1)