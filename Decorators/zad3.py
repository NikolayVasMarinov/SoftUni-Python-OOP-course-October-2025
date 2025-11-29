def even_numbers(function):
    def wrapper(numbers):
        func = function(numbers)
        return [num for num in func if num % 2 == 0]

    return wrapper