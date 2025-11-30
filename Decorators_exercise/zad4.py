from typing import Type

def type_check(match_type: Type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if any(not isinstance(parameter, match_type)
                   for parameter in list(args) + list(kwargs.values())):
                return "Bad Type"

            return func(*args, **kwargs)

        return wrapper

    return decorator