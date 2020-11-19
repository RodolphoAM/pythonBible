def contains_factory(i):
    def contains(lst):
        return i in lst
    return contains

contains_15 = contains_factory(15)
print(contains_15([1, 2, 3, 15]))

def counter_factory():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def counter_factory_2():
    count = 0
    def getter():
        nonlocal count
        return count
    def incrementer():
        nonlocal count
        count += 1
    return (incrementer, getter)

