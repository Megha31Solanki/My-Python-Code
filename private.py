class Employee:
    def __init__(self,name, age ):
        self.name=name
        self.__age=age

    def Show_salary(self):
        print(self.__age)

emp=Employee("rose",34)
print(emp.name)
emp.Show_salary()

#print(emp.__age) not accessed

        