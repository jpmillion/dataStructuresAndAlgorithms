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

def isPrime?(n)
    return 'invalid input' if n < 0
    return false if n < 2 || (n % 2 == 0 && n != 2)

    squareRoot = Math.sqrt(n).floor

    (3..squareRoot).step(2) { |num| return false if n % num ==0 }

    true
end

for i in -1..10 do
    puts i.to_s + ': ' + fib(i).to_s
end

for i in -1..10 do
    puts i.to_s + ': ' + fac(i).to_s
end

(-1...100).step { |num| puts num.to_s + ': ' + isPrime?(num).to_s }