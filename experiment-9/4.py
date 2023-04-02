#wap to print each line of a file in reverse order.
f=open("exp4.txt", "r")
for line in reversed(list(f.readlines())):
    print(line.rstrip())