from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
            self.warehouse.append(computer)

            return computer.configure_computer(processor, ram)

        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
            self.warehouse.append(computer)

            return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        for computer in self.warehouse:
            if (computer.price <= client_budget and
                    computer.processor == wanted_processor and
                    computer.ram >= wanted_ram):

                sold_computer = computer
                break

        else:
            raise Exception("Sorry, we don't have a computer for you.")

        self.warehouse.remove(sold_computer)
        self.profits += client_budget - sold_computer.price
        return f"{sold_computer} sold for {client_budget}$."
