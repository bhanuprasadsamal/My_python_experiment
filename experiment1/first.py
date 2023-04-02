str=input("enter the sentence")
lis=str.split()
l=len(lis)

for i in range(0,l-1,1):
    for j in range(i,l):
        a=lis[j]
        str1=(a[::-1])
        lenn1=len(a)
        if(lenn1%2==0):
            print(str1[lenn1-1])
        else:
            break
        
        # else:
        #     print("not")



        # list=s.split()
# length=len(list)
# for j in range (0,length,1):
      
#   for i in range(j,length,1):
#             len1=len(list[i])
#             if(len1%2==0):
#                   print(list[i])
#                   break
#             else:
#                   print("this is include odd no. of characters")


