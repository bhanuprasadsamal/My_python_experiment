# Wapp to input a paragraph and print the first position of each word

s=input("Enter a sentence: ")
print(0,end=" ")
for i in range(len(s)):
    if s[i]==" ":
        print(i+1,end=" ")

