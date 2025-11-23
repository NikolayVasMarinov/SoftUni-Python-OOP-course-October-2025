class reverse_iter:
    def  __init__(self, iterable: iter):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.iterable[self.index]
        else:
            raise StopIteration