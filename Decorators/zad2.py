def vowel_filter(function):
    def wrapper():
        func = function()
        func = list(filter(lambda x: x.lower() in ["e", "a", "o", "u", "y", "i"], func))
        return func

    return wrapper