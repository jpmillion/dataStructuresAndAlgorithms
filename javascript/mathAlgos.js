function fib(n) {
    if (n < 1) return 'invalid input'

    let nMinusOne = 1;
    let nMinusTwo = 0;

    for (let i = 2; i < n; i++) {
        const temp = nMinusTwo;
        nMinusTwo = nMinusOne;
        nMinusOne += temp;
    }

    return nMinusOne + nMinusTwo;
}

function fac(n) {
    if (n < 0) return 'invalid input';

    let product = 1;

    for (let i = n; i > 1; i--) {
        product *= i;
    }

    return product;
}

function isPrime(n) {
    if (n < 0) return 'invalid input';
    if (n < 2 || (n % 2 == 0 && n !== 2)) return false;

    const squareRoot = Math.floor(Math.sqrt(n));

    for (let i = 3; i <= squareRoot; i += 2) {
        if (n % i === 0) return false;
    }

    return true;
}

for (let i = -1; i < 10; i++) {
    console.log(fib(i));
}

for (let i = -1; i < 11; i++) {
    console.log(fac(i));
}

for (let i = -1; i < 100; i += 2) {
    console.log(i + ': ' + isPrime(i));
}
