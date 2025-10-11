class Animal:
    def sound(self):
        print("Generic animal sounds")


class Dog(Animal):
    def sound(self):
        print("Woof, Woof!")

class Frog(Animal):
    def sound(self):
        print("Ribbit, Ribbit!")


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

frog = Frog()
frog.sound()