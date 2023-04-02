# open the exiting file "giet.txt and count the vowel"
f=open("giet.txt",'r')
s=f.read()
l=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in s:
    if i in l:
        c=c+1
print(s)
print("No of vowel is : ",c)
f.close()