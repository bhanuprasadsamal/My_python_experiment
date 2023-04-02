def evenFibSum(li) :
    if(li<2):
        return 0
    f1=0
    f2=2
    sum=f1+f2
    while(f2<=li):
        f3=4*f2+f1
        if(f3 > li):
            break
        f1=f2
        f2=f3
        sum= sum+f2
    return sum
li=1000
print(evenFibSum(li))
    	