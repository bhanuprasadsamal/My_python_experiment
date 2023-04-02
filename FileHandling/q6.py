# wapp to read the content of "sec_c.txt" file line by line
f=open("sec_c.txt",'r')
line1=f.readline()
print(line1,end=' ')
line2=f.readline()
print(line2,end=' ')
line3=f.readline()
print(line3,end=' ')
f.close()