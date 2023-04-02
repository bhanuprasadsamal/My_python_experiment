#write a python program to input 3 integer and find out the greatest

x= int(input("Enter x : "))
y= int(input("Enter y : "))
z= int(input("Enter z : "))
if(x>y and x>z):
    print("%d is big",x)
elif(y>z):
    print("%d is big ",y)
else:
    print("%d is big ",z)
