#wapp to print the no. of words,lines,character present in the given file.print
import os,sys
fname=input("Enter file name:")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("the no. of lines:",lcount)
print("the no. of words:",wcount)
print("the no. of characters:",ccount) 