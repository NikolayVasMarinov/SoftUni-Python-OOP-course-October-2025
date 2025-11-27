class sequence_repeat:
    def __init__(self, string: str, number: int):
        self.string = string
        self.number = number
        self.current = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.number:
            raise StopIteration

        index = self.current % len(self.string)
        self.current += 1
        return self.string[index]