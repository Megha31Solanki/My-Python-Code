class Dog:
    species="canine" #class attribute

    def __init__(self,name,age): # constructor call
        self.name=name #instance attribute
        self.age=age #instancce attribute

# creating object
dog1=Dog("tommy",12)
print(dog1.name,dog1.age) #accessing instance attribute
print(dog1.species)        #accessing class attributes