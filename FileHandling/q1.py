#WAPP TP CRAET A TEXT FILE ABCD.TXT AND WRITE SOME TEXT INTO THE FILE
f=open("abcd.txt",'w')
f.write("HII\n")
f.write("how are you\n")
f.write("sir")
print("Date written in the file is succesive....")
f.close()  #not nessesary