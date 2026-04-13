class Parent:
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def __init__(self, age, name):
        super().__init__(name)
        self.age =age
        print(f"name {self.name}, age:{self.age}")


child1 = Child("asas", 9)