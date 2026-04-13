class Person:
    count = 0 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Person.count +=1

person1 = Person("me", 23)
person2 = Person('you', 22)

print(f"Person count {Person.count}")