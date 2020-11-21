def divide(num1, num2):
    assert num2 > 0, "Divisor cannot be zero!"
    return num1/num2

a1 = divide(12, 4)
#print(a1)
#a1 = divide(12, 0)
#print(a1)

import math

def sqrt(a,b,c):
    assert b**2 >= 4*1*c, "Cannot find square root of negative number, found %s < %s"%(b**2, 4*a*c)
    return math.sqrt(b**2 >= 4*1*c)

print(sqrt(10, 12, 3))

def apply_discount(product, discount):
    price = int(product['price']*(1 - discount))
    assert 0 <= price <= product['price']
    return price
