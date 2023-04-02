#Generate fibonacci series between 0 to 1000.then find the sum of even valued terms
a=-1
b=1
s=0
c=0
c=c+b
while(c<=1000):
    c=a+b
    if(c%2==0):
        s=s+c
    a=b
    b=c
print("The sum of Even term ",s)