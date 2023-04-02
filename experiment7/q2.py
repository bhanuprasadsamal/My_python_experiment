#write a python program to input an integer and check it is perfect or not unsing function
def perfect(n):
    i,sum=1,0
    while(i<n):
        if(n%i==0):
            sum=sum+i
        i=i+1
    if(sum==n):
        print ("perfect")
    else:
        print("Not perfect")
n=int(input("Enter a integer: "))
perfect(n)