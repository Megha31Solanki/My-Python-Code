class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def show_role(self):
        print(self.name)

emp=Employee("megha")
print(emp.name)
                