from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    EXTRA_CONSUMPTION = 0.9

    def drive(self, distance: float) -> None:
        needed = distance * (self.fuel_consumption + self.EXTRA_CONSUMPTION)

        if needed <= self.fuel_quantity:
            self.fuel_quantity -= needed

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_CONSUMPTION = 1.6
    REFUEL_EFFICIENCY = 0.95

    def drive(self, distance: float) -> None:
        needed = distance * (self.fuel_consumption + self.EXTRA_CONSUMPTION)

        if needed <= self.fuel_quantity:
            self.fuel_quantity -= needed

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY