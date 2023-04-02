# WAPP TO INPUT A SENTENCE MAKE REVERSE TO EACH WORD OF THE SENTENCE
s=input("Enter a sentence : ")
l=s.split()
for i in range(len(l)):
    print(l[i][::-1])