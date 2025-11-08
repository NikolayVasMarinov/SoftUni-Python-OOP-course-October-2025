class Vet:
    animals: list[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: list[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space == 0:
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        Vet.space -= 1

        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        Vet.space += 1

        return f"{animal_name} unregistered successfully"

    def info(self) -> str:
        return (f"{self.name} has {len(self.animals)} animals. "
                f"{Vet.space} space left in clinic")