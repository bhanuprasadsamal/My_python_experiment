# creat a customer class 
import sys
class customer:
    def __init__(self,name,bal=0.0):
        self.name =name
        self.bal=bal
    def deposite(self,amt):
        self.bal+=amt
        print("The balance after deposite: ",self.bal)
    def withdraw(self,amt):
        if(amt>self.bal):
            print("Insufficient balance")
            sys.exit()
        self.bal=amt
        print("Withdraw after ",self.bal)
name=input("Enter Name: ")
c=customer(name)
while(True):
    print('d-Deposite\nw-Withdraw\ne-Exit')
    option=input("Enter the option: ")
    if(option=='d'or option=='D'):
        amt=float(input("Enter the deposite amount: "))
        c.deposite(amt)
    elif(option(option=='w'or option=='W')):
        amt=float(input("Enter the Withdraw amount: "))
        c.withdraw(amt)
    elif(option(option=='e'or option=='E')):
        print("Thanks for banking .Have a good day!")
        sys.exit()
    else:
        print("Please enter tha valid option !!")
    