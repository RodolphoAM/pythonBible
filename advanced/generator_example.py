def numberGenerator(n):
    try:
        number = 0
        while number < n:
            yield number
            number += 1
    finally:
        yield n

myGenerator = numberGenerator(3)
print(next(myGenerator))
print(next(myGenerator))
print(next(myGenerator))

g = numberGenerator(10)
counter = 0
while counter < 10:
    print(next(g))
    counter += 1

#newGenerator = numberGenerator(23)
#print(next(newGenerator))
