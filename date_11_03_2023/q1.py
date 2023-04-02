# WAPP TO GENERATE N INTEGER NUMBER WITH IN THE RANGE 100 TO 200 AND FINDOUT SUM AND  AVERAGE
from random import*
sum=0
n=int(input("Enter a integer: "))
for i in range(n):
    s=randint(100,200)
    sum=sum + s
    print(s)
avg=sum/n
print("Sum is : ",sum)
print("Average is : ",avg)

