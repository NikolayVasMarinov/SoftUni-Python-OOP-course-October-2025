class Circle:
    pi: float = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        return self.radius ** 2 * self.pi

    def get_circumference(self) -> float:
        return 2 * self.pi * self.radius