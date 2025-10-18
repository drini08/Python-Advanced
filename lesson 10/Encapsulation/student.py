class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name


    def set_name(self, name):
        self.__name = name


    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age = age

student1 = Student("SGA", 26)

print("Current MVP Name:", student1.get_name())
student1.set_name("Antman")
print("Actual MVP Name:", student1.get_name())

print("SGA Age:", student1.get_age())
student1.set_age("24")
print("Antman Age:", student1.get_age())


