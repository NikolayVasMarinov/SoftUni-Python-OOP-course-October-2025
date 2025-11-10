class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel: float = fuel
        self.horse_power: int = horse_power

    def drive(self, kilometers: float) -> None:
        needed_fuel = self.fuel_consumption * kilometers

        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel