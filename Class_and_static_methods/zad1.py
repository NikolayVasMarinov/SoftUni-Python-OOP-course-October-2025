from math import prod


class Calculator:
    @staticmethod
    def add(*args) -> float:
        return sum(args)

    @staticmethod
    def multiply(*args) -> float:
        return prod(args)

    @staticmethod
    def divide(*args) -> float:
        return args[0] / Calculator.multiply(*args[1:])

    @staticmethod
    def subtract(*args) -> float:
        return args[0] - Calculator.add(*args[1:])