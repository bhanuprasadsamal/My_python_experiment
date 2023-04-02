#wap to combine lists that combine two lists into a dictionary.
list1=["apple", "orange", "banana"]
list2=[1,2,3]
print("list 1 :",list1)
print("list 2 :",list2)
d={}
for key in list1:
    for value in list2:
        d[key]=value
        list2.remove(value)
        break
print("Dictionary from lists :",d) 
