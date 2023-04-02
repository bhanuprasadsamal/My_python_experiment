#creat a file from run time
f=open("practice2.txt",'a')
d=input("Enter your name: ")
f.write(d)
print("Thanks for your name.")
f.close()