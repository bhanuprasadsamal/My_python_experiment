P= int(input("enter the principal : "))
R= int(input("enter the rate of interest : "))
T= int(input("enter the time : "))
s=(P*T*R)/100
c=P*((1+R)**T)-P
print("simple interest is : ",s)
print("compound is : ",c)