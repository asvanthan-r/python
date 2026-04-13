from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, len, width):
        self.len = len
        self.width = width
    def area(self):
        return self.len*self.width
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
def print_area(shape:Shape):
    print(shape.area())

print_area(Rectangle(4, 5))
print_area(Square(4))