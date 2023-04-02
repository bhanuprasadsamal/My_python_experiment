#wap to count the number of characters in the string and store them in a dictionary data structure.
n = input("Enter a string:")
dict = {}
for i in n:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
print(type(dict))