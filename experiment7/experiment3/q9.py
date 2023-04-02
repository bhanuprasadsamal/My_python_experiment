#amstrong or not
n=int(input("Enter a number : "))
sum=0
temp=n
while(n!=0):
    d=n%10
    sum=sum+d**3
    n= n//10
if(temp == sum):
    print("Amstrong")
else:
    print("Not amstrong")