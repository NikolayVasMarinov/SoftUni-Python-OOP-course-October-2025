class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def status(self) -> str:
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"

    def water(self, quantity: int) -> None:
        self.is_happy = quantity >= self.water_requirements