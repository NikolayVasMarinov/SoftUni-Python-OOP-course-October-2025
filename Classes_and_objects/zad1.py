class Vehicle:
    def __init__(self, mileage: float, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: list[str] = []