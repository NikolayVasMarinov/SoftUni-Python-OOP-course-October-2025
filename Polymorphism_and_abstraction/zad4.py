from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius

    def calculate_area(self) -> float:
        return self.__radius ** 2 * pi

    def calculate_perimeter(self) -> float:
        return self.__radius * 2 * pi

class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.__height = height
        self.__width = width

    def calculate_area(self) -> float:
        return self.__height * self.__width

    def calculate_perimeter(self) -> float:
        return (self.__height + self.__width) * 2
