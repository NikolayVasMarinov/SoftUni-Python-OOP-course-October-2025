from abc import ABC, abstractmethod

from project.food import Food, Meat
from project.animals.animal import Animal


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @abstractmethod
    def feed(self, food: Food) -> str | None:
        pass

    def __repr__(self):
        return (f"{self.__class__.__name__} [{self.name}, {self.wing_size}, "
                f"{self.weight}, {self.food_eaten}]")

class Owl(Bird):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD

class Hen(Bird):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    def feed(self, food: Food) -> None:
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD