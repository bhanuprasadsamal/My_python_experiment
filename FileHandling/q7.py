# Wapp to raed all the lines from "abc.txt" file
f=open("abc.txt",'r')
lines=f.readline()
for line in lines:
    print(line,end=' ')
f.close()