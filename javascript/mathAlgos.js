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

for (let i = -1; i < 10; i++) {
    console.log(fib(i));
}

for (let i = -1; i < 11; i++) {
    console.log(fac(i));
}
