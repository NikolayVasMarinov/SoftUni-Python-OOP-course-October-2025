class vowels:
    def __init__(self, string: str):
        self.string = string
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.string):
            raise StopIteration

        if self.string[self.index].lower() in ["a", "e", "o", "i", "u", "y"]:
            return self.string[self.index]

        else:
            return self.__next__()