class Student:
    school_name = "Digital School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course  = course

student1 = Student("Kayla", 22, "Scratch")
student2 = Student("Jack", 19, "Code 3")
print(student1.course)
print(student2.course)