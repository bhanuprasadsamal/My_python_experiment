dict1,dict2={},{}
n=int(input("Enter length of dictionaries : "))
for i in range(n):
    key,value=input("Enter key and value : ").split()
    dict1.update({key:value})
for i,j in dict1.items():
    dict2.update({j:i})
print(dict1,"\n",dict2)
