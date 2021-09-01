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