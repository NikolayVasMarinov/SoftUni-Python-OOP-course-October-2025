from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.astronauts: list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not all(c.isalnum() or c == "-" for c in name):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")

        self.__name = name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("A station cannot have a negative capacity!")

        self.__capacity = capacity

    def calculate_total_salaries(self) -> str:
        return f"{sum(a.salary for a in self.astronauts):.2f}"

    def status(self) -> str:
        astronaut_ids = (" #".join(sorted([a.id_number for a in self.astronauts]))
                         if self.astronauts else "N/A")

        return (f"Station name: {self.name}; Astronauts: {astronaut_ids}; "
                f"Total salaries: {self.calculate_total_salaries()}")

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass