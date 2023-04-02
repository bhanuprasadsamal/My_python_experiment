#WAPP TO CRAET A FILE "ABC.TXT" AND WRITE 4 LINES INTO THE FILE
f=open("abc.txt",'a')
list=["apple\n","banana\n","mango\n"]
f.writelines(list)
print("abc.txt ixs complete! ")
f.close()
 