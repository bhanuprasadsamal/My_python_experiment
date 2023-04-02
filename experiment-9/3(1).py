""" WAPP to count frequency of characters in a given file.
    Can you use character frequency to tell whether the given
    file is a Python file,C file or text file. """

fname=input("Enter file name : ")
file=open(fname,"r")
a=[]
d={}
for i in file:
    for j in range(0,len(i)):
        a.append(i[j]) 
for i in a: 
    if i in d: 
        d[i]=d[i]+1
    else: 
        d[i]=1
print(d)

l=fname.split(".")
if(l[1]=="txt"):
    print("It is a text file")
elif(l[1]=="cpp"):
    print("It is a C++ program file")
elif(l[1]=="py"):
    print("It is a Python program file")
else:
    print("It is a C program file")