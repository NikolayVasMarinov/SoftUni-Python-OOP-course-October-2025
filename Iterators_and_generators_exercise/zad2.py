class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.dictionary):
            raise StopIteration

        item = self.dictionary[self.count]
        self.count += 1
        return item