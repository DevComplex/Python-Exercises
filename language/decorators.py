from time import time

class Decorators:
    def __init__(self):
        pass

    def add_n(self, n):
        def decorator(func):
            def inner(*args, **kargs):
                return func(*args, **kargs) + n
            return inner
        return decorator

    def timer(self, func):
        def inner(*args, **kargs):
            before = time()
            res = func(*args, **kargs)
            after = time()
            print("Function ran in", after - before)
            return res
        return inner

    def run_n_times(self, n):
        def decorator(func):
            def inner(*args, **kargs):
                for i in range(n):
                    yield func(*args, **kargs)
            return inner
        return decorator

decs = Decorators()

@decs.timer
@decs.add_n(10)
def add(x, y):
    return x + y

@decs.run_n_times(3)
@decs.timer
def sub(x, y):
    return x - y

def main():
    res = add(5, 10)

    print(res)

    for val in sub(5, 5):
        print(val)

if __name__ == "__main__":
    main()