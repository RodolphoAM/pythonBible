import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
numbers = [23, 20, 44, 32, 7, 12]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]

#print(list(itertools.chain(letters, booleans, decimals)))
#print([(i * 0.01) + 10 for i in range(100)])
#print(itertools.count(10, 0.25))
#print(list(itertools.filterfalse(lambda x: x % 2, numbers)))
#print(list(itertools.filterfalse(lambda x: x < 20, itertools.count(10, 0.25))))

#print(list(itertools.compress(letters, booleans)))
