#reverse
n=int(input("Enter an integer: "))
temp=0
while(n!=0):
    digit=n% 10
    temp=temp*10+digit
    n=n//10

print("reverse no. ",temp)