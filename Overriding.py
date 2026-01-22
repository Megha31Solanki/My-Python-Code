class Animal:
    def sound(self):
        return "some generaric sound"
    
class Dog (Animal):
    def sound(self):
        return "Bark"
    
class Cat (Animal):
    def sound(self):
        return "meow"

animals=[Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.sound())        
            