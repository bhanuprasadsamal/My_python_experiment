#Wapp to print the series 1 2 4 7 11 16 ..............n
n=int(input("enter the n value : "))
# for i in range(0,n+1,1):
#     j=1
#     j=j+i
# #     print(j,end=" ")
#  print("First Series:")
#     for i in range(1, 41, 3) :
#         print(i, end = ' ')
# for i in range(1,n,2):
#     print(i, end = ' ')
j=1
for i in range(n):

    j=j+i
    print(j,end=' ')