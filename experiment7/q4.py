#write a python program to creat a function which access a sentence and then convert capitalized the 1st a 
# letter of each word in sentence .Also generate a list with reverse sequence of words and count the no.of words
def capitalize(str):
    str=str.split()
    y=""
    for i in range(len(str)):
        str[i]=str[i].capitalize()
        y=y+(str[i]+" ")
    y=y.split()
    print("In capitalize : ",str)
    print("Reverse is ",y[::-1])
    print("No. of words is ",len(y))
str=input("Enter a sentence : ")
capitalize(str)
