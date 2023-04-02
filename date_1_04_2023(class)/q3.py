#creat a university class having the member name and code the create another two calss teacher and student which derives the property from university class which derives from property teacher and student
class University:
    def __init__(self):
        self.name="GIETU"
        self.code=420
class Teacher(University):
    def __init__(self):
        super().__init__("GIETU",420)
        self.teachername="hari"
        self.teacherid=1234
class Student(University):
    def __init__(self):
        self.studentname="bhanu"
        self.rollno=142
class Test(Teacher,Student):
    def __init__(self):
        University.__init__(self)
    def check(self):
        if(self.name=="GIETU"):
            print("Both are from the same university")
        else:
            print("Both are not from the same university!!!")





