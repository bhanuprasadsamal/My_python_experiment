# WITH STATEMENT EXAMPLE
with open("abc.txt",'w') as f:
    f.write("Durga\n")
    f.write("Hero\n")
    f.write("siva\n")
    print("Is the file is closed: ",f.closed)  #give false because writen inside the with statement
print("Is the file is cloed: ",f.closed)