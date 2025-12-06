from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    INITIAL_CAPACITY = 5
    SALARY_INCREASE = 5000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization != "ScientistAstronaut":
                continue

            if a.salary <= min_value:
                a.salary += self.SALARY_INCREASE