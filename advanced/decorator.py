def some_func():
    print("Hey, guys!")

def my_decorator(func):
    def inner():
        print("Before function!")
        func()
        print("After function!")

    return inner

print("Some function:")
some_func()

decorated = my_decorator(some_func)

print("Function with decorator:")
print(decorated())
