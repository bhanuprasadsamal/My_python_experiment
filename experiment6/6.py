l1=list(input("Enter fruits name : ").split())
l2=[]
for i in l1[::-1]:
    print(i,"-",len(i))
    l2.append(i[::-1])
l2.reverse()
print(l2)
