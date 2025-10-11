class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Generic animal sounds")

    def description(self):
        print(f"This animal is named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof, Woof!")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow, Meow!")

    def description(self):
        super().description()
        print(f"Color: {self.color}")


animal = Animal("Jamie")
dog = Dog("Rexy", "German Shepherd")
cat = Cat("Pablo", "Grey")

dog.sound()
dog.description()
cat.sound()
cat.description()







