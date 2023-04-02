#
from random import*
max=0
min=1
l=[]
for i in range(10):
    y=random()
    l.append(y)
    if(y>max):
        max=y
    if(y<min):
        min=y
print(l)
print("the maximum is : ",max)
print("the min is : ",min)