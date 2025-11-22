from project.food import Food, Meat
from project.animals.animal import Bird


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

    def feed(self, food: Food) -> str | None:
        if not isinstance(food, Food):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE_PER_PIECE_OF_FOOD