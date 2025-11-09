from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    @staticmethod
    def teach() -> str:
        return "teaching..."