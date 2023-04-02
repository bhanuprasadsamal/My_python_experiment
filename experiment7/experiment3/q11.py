
n=int(input("Enter n"))
temp=n
rev=0
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("palindrom")
else:
    print("not plindrom")

