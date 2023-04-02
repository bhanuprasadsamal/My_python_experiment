#write a recursive function to find the largest element in a list of number.
def largest(A,n):
    if(n==1):
        return A[0]
    return max(A[n-1],largest(A,n-1))
A=[1,4,23,6,-35,9,2]
n=len(A)
print(largest(A,n))
