from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"The area of square is: {self.side * self.side} cm2")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"The area of the Circle is: {3.14*self.radius*self.radius} cm2")

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        print(f"The area of Triangle is: {0.5*self.base*self.height} cm2")


class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Square(5),Circle(4), Triangle(2,3), Pizza("Tomato", 8)]

for shape in shapes:
    shape.area()