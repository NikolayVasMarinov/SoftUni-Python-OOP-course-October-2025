import time


class exec_time:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()

        print(f"{self.func.__name__} took {end - start:.6f} seconds")

        return result