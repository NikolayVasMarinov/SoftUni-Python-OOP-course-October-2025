from operator import index


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person") -> "Person":
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name: str, people: list[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other: "Group") -> "Group":
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

    def __iter__(self):
        for i, p in enumerate(self.people):
            yield f"Person {i}: {str(p)}"

    def __getitem__(self, i: int):
        return f"Person {i}: {str(self.people[i])}"