class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor")
    def display_info(self):
        print(f"Name: \'{self.name}\'\nAge: {self.age}")



person1 = Person("Asvanthan", 28)
person1.display_info()