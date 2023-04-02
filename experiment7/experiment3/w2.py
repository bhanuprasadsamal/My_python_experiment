# prime or not
n=int(input("Enter an integer: "))
c=0
i=1
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("{}is a prime".format(n))
else:
    print("{}is not a prime".format(n))