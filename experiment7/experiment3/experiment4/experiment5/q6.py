#Wapp to inputa sentence and remove the duplicate charecter
s=input("Enter a sentence : ")
l=[i for i in s]
for i in range (len(l)):
    if(i!=l.index(l[i])):
        l[i]=" "
    print(l[i],end=' ')
