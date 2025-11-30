def cache(function):
    # class Cache:
        #def __init__(self, func):
           # self.func = func
            #self.log: dict[int, int] = {}

        #def __call__(self, n):
           # if n in self.log:
            #    return self.log[n]

          #  result = self.func(n)
         #   self.log[n] = result
         #   return result

  #  return Cache(function)

    def wrapper(n):
        if n not in wrapper.log:
            wrapper.log[n] = function(n)
        return function(n)

    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n: int):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)