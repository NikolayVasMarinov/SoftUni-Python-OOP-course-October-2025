from project.animal import Animal
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.worker import Worker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)

        if worker is None:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        salaries_paid = sum(w.salary for w in self.workers)

        if self.__budget < salaries_paid:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_paid
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        price_paid = sum(a.money_for_care for a in self.animals)

        if self.__budget < price_paid:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= price_paid
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        categories = [Lion, Tiger, Cheetah]

        result = [f"You have {len(self.animals)} animals"]

        for class_ in categories:
            items = [a for a in self.animals if isinstance(a, class_)]
            result.append(f"----- {len(items)} {class_.__name__}s:")
            result.extend(str(a) for a in items)

        return "\n".join(result)

    def workers_status(self) -> str:
        categories = [Keeper, Caretaker, Vet]

        result = [f"You have {len(self.workers)} workers"]

        for cls in categories:
            workers = [w for w in self.workers if isinstance(w, cls)]
            result.append(f"----- {len(workers)} {cls.__name__}s:")
            result.extend(str(w) for w in workers)

        return "\n".join(result)