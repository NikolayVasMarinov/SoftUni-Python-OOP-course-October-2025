def read_next(*args):
    for iterable in args:
        for char in iterable:
            yield char