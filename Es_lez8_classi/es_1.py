#Riccardo Giacalone

from abc import ABC, abstractmethod


"""
Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
"""

class Shape(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    PI : float = 3.14159265358

    def __init__(self,radius:float) -> None:
        super().__init__()
        self.radius: float = radius

    def area(self, PI) -> float:
        area : float = (self.radius * self.radius) * PI
        return area
    
    def perimeter(self, PI):
        perimeter: float = (self.radius * 2) * PI
        return perimeter
    
class Rectancle(Shape):

    def  __init__(self, length:float, width:float) -> None:
        super().__init__()
        self.length: float = length
        self.width: float = width

    def area(self):
        area : float = self.length * self.width
        return area
    
    def perimeter(self):
        perimeter: float = (self.length + self.width) * 2
        return perimeter