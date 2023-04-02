#write a python program to calculate the geometric sum of n-1 using a recursive function
def geo_sum(n):
    if(n<0):
        return 0
    else:
        return 1/(pow(2,n))+geo_sum(n-1)
print(geo_sum(4))