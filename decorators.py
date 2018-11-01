

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@do_twice
def say_hello(name):
    print("Hello {name}")


@do_twice
def hello(who):
    print("hello {who}")


say_hello("Hello")

hello("World")

