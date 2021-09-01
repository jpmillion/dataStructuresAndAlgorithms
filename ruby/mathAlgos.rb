def fib(n)
    return 'invalid input' if n < 1

    nMinusTwo = 0
    nMinusOne = 1

    for i in 2...n do
        nMinusTwo, nMinusOne = nMinusOne, nMinusOne + nMinusTwo
    end

    nMinusOne + nMinusTwo
end

def fac(n)
    return 'invalid input' if n < 0

    product = 1

    for i in (2..n) do
        product *= i
    end

    product
end

for i in -1..10 do
    puts i.to_s + ': ' + fib(i).to_s
end

for i in -1..10 do
    puts i.to_s + ': ' + fac(i).to_s
end