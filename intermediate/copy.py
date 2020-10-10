lst1 = ['a', 'b', ['ab', 'ba']]
lst2 = lst1
lst3 = lst1[:]

lst2[0] = 'c'
lst3[0] = 'x'

print(lst3)
print(lst2)
print(lst1)