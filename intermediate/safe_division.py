def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

def safe_division_b(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

def safe_division_c(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1, 10**500, True, False)
print(result)
result2 = safe_division_b(1, 0, ignore_zero_division=True)
print(result2)
result3 = safe_division_c(1, 0, ignore_zero_division=True)
print(result2)
