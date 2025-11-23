class custom_range:
    def  __init__(self, start: int, end: int):
        self.current = start
        self.end = end

#    def __iter__(self):
   #     for num in range(self.start, self.end + 1):
      #      yield num

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        else:
            raise StopIteration