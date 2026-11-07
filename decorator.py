def my_decorator(func):

    def wrapper():
        print("Function is starting")
        func()
        print("Function is finished")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)

say_hello()