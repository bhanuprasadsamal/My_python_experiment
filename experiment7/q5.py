
#write a program that accepts a string and a number x.Then print each charecter of x time .(paperdoll problem ).
def fun(s):
    for i in range(0,len(s)+1):
        print(s[i]*3,end=' ')
s=input("Enter a string : ")
fun(s)