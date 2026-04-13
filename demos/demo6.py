class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

student1 = Student("asvanthan", 2, 28)

print(getattr(student1, 'age'))

setattr(student1, 'age', 22)

print(getattr(student1, 'age'))

print(hasattr(student1, 'age'))

delattr(student1, 'age')

print(hasattr(student1, 'age'))

print("class", Student.__name__)
print("Module", Student.__module__)
print("bases", Student.__bases__)
print("dict", Student.__dict__)