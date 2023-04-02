#WAPP  swap with outusing 3rd variable
a=int(input("enter the a value"))
b=int(input("enter the b vlaue"))
print("before swap the value of a and b is : ",a,b)
a=a+b
b=a-b
a=a-b
print("after swap the a and b is : ",a,b)