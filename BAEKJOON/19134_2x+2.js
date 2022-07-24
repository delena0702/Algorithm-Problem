let N = require('fs').readFileSync('/dev/stdin').toString().trim();

function calc(n) {
    if (n < 3) return [null, n];
    let cnt = (n + 1n) / 2n + 1n, retval = calc((n - 2n) / 2n);
    retval.unshift(0);

    for (let i=retval.length-1; i>=2; i--)
        cnt -= retval[i];
    retval[1] = cnt;
    return retval;
}

function getOutput(arr) {
    let retval = 0n;
    for (let i=1; i<arr.length; i++)
        retval += ((BigInt(i) + 1n) / 2n) * arr[i];
    return retval;
}

console.log(getOutput(calc(BigInt(N))).toString());