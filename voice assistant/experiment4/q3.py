#Wapp to print fibonacci series upto nth term
n=int(input("Enter the n value: "))
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
