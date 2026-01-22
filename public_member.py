class Employee:
    def __init__(self,name):
        self.name=name  #public attribute

    def display_name(self): #public method
        print(self.name)

emp=Employee("john")

emp.display_name() #accesible
print(emp.name)            #accessible