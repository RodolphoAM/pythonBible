def intsfrom(i):
    while 1:
        yield i
        i += 1

def exclude_multiples(n, ints):
    for i in ints:
        if(i%n):
            yield i

def sieve(ints):
    while 1:
        prime = ints.next()
        yield prime
        ints = exclude_multiples(prime, ints)