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

for (let i = -1; i < 10; i++) {
    console.log(fib(i));
}
