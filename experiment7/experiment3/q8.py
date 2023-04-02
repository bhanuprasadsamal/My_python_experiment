# #perfect  or not
s=0
i=1
n=int(input("Enter a digit : "))
for x in range(i,n):
    if(n%x==0):
        s=s+x
if(s==n):            
    print("perfect")
else:
     print("not perfect")

