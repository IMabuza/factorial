import unittest

def fac(n):

    multiple, prod = n - 1, 1

    while multiple >= 1:
        prod = prod * multiple
        multiple = multiple - 1

    result = n * prod
    print(result)
#6!
fac(6)
