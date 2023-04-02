#write a python program to find the distance between two point(x1,y1) and (x2,y2)

import math
x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))

d=math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1,2))
print("distance is {}".format(d))