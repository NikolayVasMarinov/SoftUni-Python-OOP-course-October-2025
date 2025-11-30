def even_parameters(func):
    def wrapper(*args, **kwargs):
        def is_even_int(x):
            return isinstance(x, int) and x % 2 == 0

        if any(not is_even_int(value) for value in list(args) + list(kwargs.values())):
            return "Please use only even numbers!"

        return func(*args, **kwargs)

    return wrapper