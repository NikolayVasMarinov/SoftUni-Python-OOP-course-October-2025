from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    SPECIALIZATION = "EngineerAstronaut"
    STAMINA = 80
    STAMINA_INCREASE = 5

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.STAMINA)

    def train(self):
        if self.stamina + self.STAMINA_INCREASE > 100:
            self.stamina = 100

        else:
            self.stamina += self.STAMINA_INCREASE