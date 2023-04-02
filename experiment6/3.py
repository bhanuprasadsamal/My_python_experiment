## WAPP to find frequency of each digit in a given number.

num=int(input("Enter a number : "))
s=str(num)
l=[]
for i in s:
    if(i+":"+str(s.count(i))not in l):
        l.append(i+":"+str(s.count(i)))
print(l)
