class custom_range:
    def  __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        for num in range(self.start, self.end + 1):
            yield num