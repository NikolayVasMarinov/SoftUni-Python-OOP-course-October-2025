from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

class Dog(Animal):
    @staticmethod
    def make_sound():
        return "woof-woof"

class Cat(Animal):
    @staticmethod
    def make_sound():
        return "meow"

class Chicken(Animal):
    @staticmethod
    def make_sound():
        return "cluck"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('cat'), Dog('dog')]
animal_sound(animals)

animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)