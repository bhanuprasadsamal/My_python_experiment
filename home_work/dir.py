import os
print(os.getcwd())
os.mkdir("data")
if(os.path.exists("data1")):
     print("available")
else:
     print("not")