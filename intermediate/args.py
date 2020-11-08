def print_args(*args, **kwards):
    print('Positional: ', args)
    print('Keyword: ', kwards)

def safe_division_d(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_division = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)
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


print_args(1, 2, foo="bar", stuff="meep")

div1 = safe_division_d(1, 0, ignore_zero_division=True)
print(div1)
div2 = safe_division_d(1, 0, True, False) #erro proposital; ele aceita 2 argumentos posicionais
print(div2)
div3 = safe_division_d(1, 0, unknown=True) #argumento-chave não reconhecido
print(div3)
