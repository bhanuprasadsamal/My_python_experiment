# creat a person class having name and address then derive employ class
class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
class Employee(Person):
    def __init__(self,ename,sal):
        super().__init__("Bhanu","Jajpur")
        self.ename =ename
        self.sal = sal
em=Employee(142,5000)
print(em.__dict__)

    
    