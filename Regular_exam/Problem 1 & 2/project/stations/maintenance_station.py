from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    INITIAL_CAPACITY = 3
    SALARY_INCREASE = 3000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def update_salaries(self, min_value: float):
        for a in self.astronauts:
            if a.specialization != "EngineerAstronaut":
                continue

            if a.salary <= min_value:
                a.salary += self.SALARY_INCREASE