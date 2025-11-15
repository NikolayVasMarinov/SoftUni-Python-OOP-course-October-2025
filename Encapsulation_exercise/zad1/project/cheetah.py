from project.animal import Animal


class Cheetah(Animal):

    def __init__(self, name: str, gender: str, age: int):
        money_to_be_cared_for = 60
        super().__init__(name, gender, age, money_to_be_cared_for)