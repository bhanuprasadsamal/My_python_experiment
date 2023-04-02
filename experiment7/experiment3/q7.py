#find GCD
x=int(input("Enter the 1st no. : "))
y=int(input("Enter the 2nd no. : "))
while(x!=y):
    if(x>y):
        x=x-y
    else:
        y=y-x
print("GCD is : ",x)