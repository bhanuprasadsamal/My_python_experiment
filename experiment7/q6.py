#write a recursive function to input a integer n and generate fibonacci series upto nth term.
def fibo(a,b,n):
    if(n==0):
        return
    else:
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        fibo(a,b,n-1)
n=int(input("Input n : "))
fibo(-1,1,n)