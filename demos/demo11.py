class Parent:
    def __init__(self):
        print("parent constaructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

child1 =Child()