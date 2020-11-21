"""
try:
    f = open("somefile.txt", "r")
    print(f.read())
    f.close()
except IOError:
    print("file not found")

try:
    num1, num2 = eval(input("Enter two numbers separated by coma: "))
    result = num1/num2
    print("Result: %.2f"%result)
except ZeroDivisionError:
    print("Division by zero error!")

#raising exceptions
def enter_age(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age%2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enter_age(num)
except ValueError:
    print("Only positive integers allowed")
except:
    print("Something's wrong")
"""

class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age

def enter_age_2(age):
    if age < 0:
        raise NegativeAgeException("Only positive numbers!")
    if age%2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enter_age_2(num)
except NegativeAgeException:
    print("Only positive numbers!")
except:
    print("Something's wrong")
