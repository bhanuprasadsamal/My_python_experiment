#Creat a student class having member name ,roll,mark and father income and also check his/her father income is lesss than 400000 or not .
class Student:
    def __init__(self,name,roll,mark,reg):
        self.name=name
        self.roll=roll
        self.mark=mark
        self.reg=reg
class CSE(Student):
    def __init__(self):
        super().__init__("bhanu",142,96,224)
        self.branchcode=7373728
class Test(CSE):
    def check(self):
        self.fatherinc=400000
        if(self.fatherinc<=400000 and self.mark>=95):
            print("student is eligible for scholarship")
        else:
            print("student is not eligible")
t=Test()
t.check()

