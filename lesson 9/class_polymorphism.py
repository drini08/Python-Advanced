class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Woof!")

class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes this sound: Chirp!")


dog = Dog("Buddy")
cat = Cat("Nigga")
bird = Bird("Goon")

for animal in (dog, cat, bird):
    animal.sound()
