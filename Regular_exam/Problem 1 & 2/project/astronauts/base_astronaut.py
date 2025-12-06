from abc import ABC,abstractmethod


class BaseAstronaut(ABC):
    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        self.id_number = id_number
        self.salary = salary
        self.specialization = specialization
        self.stamina = stamina

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id_number):
        if not all(c.isdigit() for c in id_number):
            raise ValueError("ID can contain only digits!")

        self.__id_number = id_number

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary must be a positive number!")

        self.__salary = salary

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        if specialization.strip() == "":
            raise ValueError("Specialization cannot be empty!")

        self.__specialization = specialization

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina):
        if not 0 <= stamina <= 100:
            raise ValueError("Stamina is out of range!")

        self.__stamina = stamina

    @abstractmethod
    def train(self):
        pass