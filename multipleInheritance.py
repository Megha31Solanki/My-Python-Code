class Person:
    def __init__(self,name):
        self.name=name

class Job:
    def __init__(self,salary):
        self.salary=salary

class Employee(Person,Job):
    def __init__(self,name,salary):
        Person.__init__(self,name)
        Job.__init__(self,salary)
emp=Employee("megha",50000)
print(emp.name,emp.salary)        
