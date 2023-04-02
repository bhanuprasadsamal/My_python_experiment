#WAPP TO CREAT A FILE X.TXT AND INPUT A STRING A RUNTIME AND WRITE A STRING INTO THE FILE
f=open("x.txt",'a')
s=input("Enter a string: ")
f.write(s)
f.close()