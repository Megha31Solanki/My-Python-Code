class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def role(self):
        print(self.name)

class Inter(Person):
    def role(self):
        print(self.name)

emp=Employee("megha")
emp.role()

intern=Inter("eva")

