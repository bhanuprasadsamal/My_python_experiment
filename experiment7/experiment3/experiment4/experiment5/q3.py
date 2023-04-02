# Wapp to input a sentence and print only the palindrom words

s=input("Enter a string : ")
l=s.split()

for i in range(len(l)):
    if(l[i]==l[i][::-1]):
        print(l[i])