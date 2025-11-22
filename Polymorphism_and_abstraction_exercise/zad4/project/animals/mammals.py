from project.food import Food, Vegetable, Fruit, Meat
from project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD

class Dog(Mammal):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD

class Cat(Mammal):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD

class Tiger(Mammal):
    WEIGHT_INCREASE_PER_PIECE_OF_FOOD = 1

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD