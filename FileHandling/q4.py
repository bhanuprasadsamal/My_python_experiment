# WAPP TO OPEN AN EXITING FILE "ABC.TXT" AND READ OUT IT'S CONTENT AND PRINTED ON THE SCREEN 
f=open("abc.txt",'r')
data =f.read()
print(data)
f.close()