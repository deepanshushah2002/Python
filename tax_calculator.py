sal=float(input("Enter a Salary"))
if sal <=150000:
    print('You does not pay any tax')
elif sal > 150000 or sal <=300000:
    tax=sal*(10/100)
    net_sal=sal-tax
    print("Your must pay salary is :",net_sal)
elif sal>300000 or sal<=500000:
    tax=sal*(20/100)
    net_sal=sal-tax
    print("Your must pay salary is :",net_sal)