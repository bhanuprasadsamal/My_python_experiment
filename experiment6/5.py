l=list(input("Enter numbers : ").split())
for i in l:
    if l.count(i)>1:
        l.remove(i)
l.sort()
print(l)
