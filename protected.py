class Employee:
    def __init__(self , name , age):
        self.name=name #public
        self._age=age  #protected

class SubEmployee(Employee):
    def show_age(self):
        print(self._age) #accessible in subclass


emp=SubEmployee("rose",30)

print(emp.name)
emp.show_age()
