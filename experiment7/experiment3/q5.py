# write a python program to input an integer and count number of its digit

num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))




