from project.vehicle import Vehicle


class Car(Vehicle):
    @staticmethod
    def drive() -> str:
        return "driving..."