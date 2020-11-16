def numberGenerator(n):
    try:
        number = 0
        while number < n:
            yield number
            number += 1
    finally:
        yield n

#myGenerator = numberGenerator(3)
#print(next(myGenerator))
#print(next(myGenerator))
#print(next(myGenerator))

#g = numberGenerator(10)
#counter = 0
#while counter < 10:
    #print(next(g))
#    counter += 1

#h = numberGenerator(10)
#next(h)
#print(h.send(5))

#newGenerator = numberGenerator(23)
#print(next(newGenerator))

def myGenerator1(n):
    for i in range(n):
        yield i

def myGenerator2(n, m):
    for j in range(n, m):
       yield j

def myGenerator3(n, m):
    yield from myGenerator1(n)
    yield from myGenerator2(n, m)
    yield from myGenerator2(n, m + 5)

print(list(myGenerator1(5)))
print(list(myGenerator2(5, 10)))
print(list(myGenerator3(0, 10)))
