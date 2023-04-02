#Wapp to find the sum of cos series
# n=int(input("enter the n value: "))
# m=1
# for i in range(0,n,2):
#     f=1
#     for j in range(1+i+1):
#         f=f*j
#     sum=sum+m*pow(x,i)/f
    # Python3 program to find the
# sum of cos(x) series

# PI = 3.142;

# def cosXSeriesSum(x, n):
	
	# here x is in degree.
	# we have to convert it to radian
	# for using it with series formula,
	# as in series expansion angle is in radian
	
	# x = x * (PI / 180.0);

	# res = 1;
	# sign = 1;
	# fact = 1;
	# pow = 1;
	
	# for i in range(1,5):
	# 	sign = sign * (-1);
	# 	fact = fact * (2 * i - 1) * (2 * i);
	# 	pow = pow * x * x;
	# 	res = res + sign * pow / fact;

	# return res;

# Driver Code
# x = 50;
# n = 5;
# print(round(cosXSeriesSum(x, 5), 6));

# This code is contributed by mits

# X = int(input("Enter the value for x:"))
# j = int(input("Enter The value for j:"))
# Sum = 0
# Fact = 1
# Sign = 1
# for i in range(1,X+1):
#      for i in range(1,j+1):
#                Fact = Fact*1
# Sum += (Sign*(X**i)/Fact*j)
# print(sum)

x = int(input("Enter the value of x: "))

sum = 0
m = 1

for i in range(1, 7) :
    fact = 1
    for j in range(1, i+1) :
        fact *= j
    term = x ** i / fact
    sum += term * m
    m = m * -1

print("Sum =", sum)

















