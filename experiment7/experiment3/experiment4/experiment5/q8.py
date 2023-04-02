#Wapp to input a sentence and count how many words are present with even no.of charecter
s=input("Enter a sentence : ")
c,l=0,s.split()
for i in l:
    if len(i)%2==0:
        c=c+1
print("no.of even words",c)