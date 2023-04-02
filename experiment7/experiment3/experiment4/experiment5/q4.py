#Wapp to input a sentence and print the even character and the odd charecter separately.

s=input("Enter a sentence : ")
even=" "
odd=""

for i in range(len(s)):
    if(i%2==0):
        even+=s[i]
    else:
        odd+=s[i]
print("Even charecter: ",even,end=" ")
print("Odd charecter: ",odd,end=" ") 