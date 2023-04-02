## Generate Fibonacci series between 0 to 1000. Then find sum of even valued terms.

a=0
b=1
print(a,b,end=' ')
c=0
sum=0
while(c<=1000):
    c=a+b
    if(c>1000):
        break
    else:
        print(c,end=' ')
        if(c%2==0):
            sum=sum+c
        a=b
        b=c
print("\nSum = ",sum)
