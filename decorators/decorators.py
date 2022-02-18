# 2 types of decorators: function decorators and class decorators
# function decorators are more common.
# Functions in Python are first-class objects. They can be defined inside another
# functions, passed as an argument to another function, and even returned from other function.

# Some typical decoror: timer to calculate the execution time of a function, debug decorator
# Check decorator to check if the arguments fulfill some requirements

# To resolve thr problems with helper, __name_, etc_
import functools

# template decorator
def template_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

# decorator
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

@start_end_decorator
def add_5(x):
    return x + 5

# decorator with argumnts
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def greet(name):
    print(f'Hello {name}')

# nested decorator
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# Class decorator
class CountCalls:
    def __init__(self, func):
        self.func  = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times.")
        return self.func(*args, **kwargs)

@CountCalls
def say_salut():
    print('Salut!')

if __name__ == "__main__":
    print("Use the regular function")
    print_name()
    print("Use the decorator function")
    #print_name = start_end_decorator(print_name)
    print_name()
    print('-'*20)
    result = add_5(5)
    print(result)
    print('-'*20)
    print(help(add_5))
    print(add_5.__name__)
    print('-'*20)
    greet('AV')
    print('-'*20)
    say_hello('AV')
    print('-'*20)
    say_salut()
    say_salut()
    say_salut()
