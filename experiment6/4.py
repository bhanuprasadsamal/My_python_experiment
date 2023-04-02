## WAPP that find the Farenheit for given Celsius from the list.

c=list(input("Enter Celsius list : ").split())
f=[]
for i in c:
    j=(float(i)*(9/5))+32
    f.append(j)
print(f)
