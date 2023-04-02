# creat a class employee having a instace member eno ,ename sal and calculate the net salary
class   Employee:
    def __init__(self,eno,ename,sal):
        self.eno =eno   
        self.ename =ename
        self.sal =sal
    def salary(self):
        BS=float(input("Input the basic salary: "))
        TA=(10*BS)/100
        DA=(15*BS)/100
        HRA=(5*BS)/100
        GS=BS+TA+DA+HRA
        PF=(12*GS)/100
        print("The Net salary is : ",GS-PF)
eno=int(input("Enter the Employee number: "))
ename=(input("Enter the Employee name: "))
sal=float(input("Enter the base salary: "))
E=Employee(eno,ename,sal)
E.salary()
        