from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in ["EngineerAstronaut", "ScientistAstronaut"]:
            raise ValueError("Invalid astronaut type!")

        if astronaut_id_number in [a.id_number for a in self.astronauts]:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        if astronaut_type == "EngineerAstronaut":
            self.astronauts.append(EngineerAstronaut(astronaut_id_number, astronaut_salary))

        elif astronaut_type == "ScientistAstronaut":
            self.astronauts.append(ScientistAstronaut(astronaut_id_number, astronaut_salary))

        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str) -> str:
        if station_type not in ["ResearchStation", "MaintenanceStation"]:
            raise ValueError("Invalid station type!")

        if station_name in [s.name for s in self.stations]:
            raise ValueError(f"{station_name} has been already added!")

        if station_type == "ResearchStation":
            self.stations.append(ResearchStation(station_name))

        elif station_type == "MaintenanceStation":
            self.stations.append(MaintenanceStation(station_name))

        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str) -> str:
        station = next((s for s in self.stations if s.name == station_name), None)

        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut = next((a for a in self.astronauts if a.specialization == astronaut_type), None)

        if astronaut is None:
            raise ValueError("No available astronauts of the type!")

        if station.capacity <= 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1

        return f"{astronaut.id_number} was assigned to {station_name}."

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int) -> str:
        total_stamina = 0

        for a in station.astronauts:
            for _ in range(sessions_number):
                a.train()

            total_stamina += a.stamina

        return (f"{station.name} astronauts have {total_stamina} total stamina "
                f"after {sessions_number} training session/s.")

    @staticmethod
    def retire_astronaut(station: BaseStation, astronaut_id_number: str) -> str:
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)

        if astronaut is None or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1

        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float) -> str:
        for station in self.stations:
            station.update_salaries(min_value)

        stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        result = ["*Space Agency Up-to-Date Report*",
                  f"Total number of available astronauts: {len(self.astronauts)}",
                  f"**Stations count: {len(stations)}; "
                  f"Total available capacity: {sum(s.capacity for s in stations)}**"]

        result.extend(s.status() for s in stations)

        return "\n".join(result)