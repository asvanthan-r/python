from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, length =0, width = 0, height =0, radius = 0):
        self.length =length
        self.width =width
        self.height = height
        self.radius = radius
    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def volume(self) -> float:
        pass
 

class rectangle(Shape):
    def area(self) -> float:
        return self.length*self.width
    def volume(self) -> float:
        return self.length*self.width*self.height
class circle(Shape):
    def area(self) -> float:
        return 3.14*self.radius*self.radius
    def volume(self):
        return 0
    
rect = rectangle(length =6, width=10, height=5)
print(f"Area: {rect.area()}, Vol: {rect.volume()}")
cir = circle(radius=5)
print(f"Area: {cir.area()}, Vol: {cir.volume()}")
