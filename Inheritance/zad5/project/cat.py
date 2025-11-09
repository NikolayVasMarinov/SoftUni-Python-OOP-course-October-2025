from project.animal import Animal


class Cat(Animal):
    @staticmethod
    def meow() -> str:
        return "meowing..."