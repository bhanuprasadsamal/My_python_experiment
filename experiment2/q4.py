#write a python program to find real roots of a quadradic equation

import math
a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))
d= b**2-(4*a*c)

if(d<0):
      print("imaginary roots ")
   
else:
     r1=(-b+math.sqrt(d))//2*a
     r2=(-b-math.sqrt(d))//2*a
     print("real roots are : {0} and {1}".format(r1,r2))

