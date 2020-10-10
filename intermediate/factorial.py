def main():
    num = int(input("Please enter a non-negative integer.\n"))
    if num < 0:
        exit()

    fact = factorial(num)
    print("The factorial of {} is {}".format(num, fact))

def factorial(num):
    if num == 0:
        return 1;
    else:
        return num * factorial(num-1)

main()