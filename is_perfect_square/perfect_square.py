from decimal import *
import cmath

def is_perfect_square(num, *, complex=False):

    if complex:
        root = cmath.sqrt(num)
        return root.real.is_integer() and root.imag.is_integer()

    try:
        if num < 0:
            return False
    except:
        raise TypeError

    digit_count = len(str(num))
    with localcontext(Context(prec=digit_count*2)):
        a = Decimal(num).sqrt()

    return True if int(a) - a == 0 else False
