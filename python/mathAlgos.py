from math import ceil, floor, sqrt


def fib(n):
    if n < 1:
        return 'Input must be positive'

    nMinusOne = 1
    nMinusTwo = 0

    for i in range(2, n):
        nMinusTwo, nMinusOne = nMinusOne, nMinusOne + nMinusTwo

    return nMinusOne + nMinusTwo

def fac(n):
    if n < 0:
        return 'invalid input'

    product = 1

    for i in reversed(range(2, n + 1)):
        product *= i

    return product

def isPrime(n):
    if n < 0:
        return 'invalid input'
        
    if n < 2 or (n % 2 == 0 and n != 2):
        return False

    squareRoot = ceil(sqrt(n))

    for i in range(3, squareRoot, 2):
        if n % i == 0:
            return False

    return True
    