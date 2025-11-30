def logged(func):
    def wrapper(*args, **kwargs):
        return (f"you called {func.__name__}"
                f"{args if args else ''}{kwargs if kwargs else ''}"
                f"\nit returned {func(*args, **kwargs)}")

    return wrapper