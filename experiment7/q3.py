#write a python program to input and integer and find out it's factorial using function
def fact(n):
    f=1
    while(n>0):
        f=f*n
        n=n-1
    print("factorial is : ",f)
n=int(input("Enter a integer: "))
fact(n)