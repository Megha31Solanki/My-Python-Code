class Person:
    def __init__(self , name):
        self.name=name

class Employee(Person):
    def show_role(self):
        print(self.name)

class Manager(Employee):
    

    def departement (self,dept):
        print(self.name,dept)

mgr=Manager("megha")
mgr.show_role()
mgr.departement("HR")                        