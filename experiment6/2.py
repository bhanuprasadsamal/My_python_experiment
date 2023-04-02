## WAPP that loops over a sequence of elements of a list,tuple,dictionary and set. 

l=["how","are","you"]
t=(1,2,3,4,5)
s={10,20,30}
d={"Name":"Bhanu","Rollno":"21CSE142","Place":"Jajpur"}
for i in l:
    print(i,end=' ')
print()
for i in t:
    print(i,end=' ')
print()
for i in s:
    print(i,end=' ')
print()
for i,j in d.items():
    print(i,":",j,end=' ')
