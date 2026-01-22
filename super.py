class Animal:
    def __init__(self,name):
        self.name=name

    def info(self):
        print(self.name)

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name) #call parent constructor
        self.breed=breed

    def details(self):
        print(self.name,self.breed)

d=Dog("buddy","kala dog")
d.info()
d.details()

