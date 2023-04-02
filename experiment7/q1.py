# write a python program to input an integer and check it is Prime or Not using Function
def prime(n):
    count =1
    i=1
    while(i<=n):
        if(n%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print("Prime")
    else:
        print("Not prime")
n=int(input("Enter a Integer: "))
prime(n)