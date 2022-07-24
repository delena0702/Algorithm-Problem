let K = 0|require('fs').readFileSync('/dev/stdin').toString().trim();
let SQRT_K = 2*Math.ceil(Math.sqrt(K));
let isPrime = new Array(SQRT_K + 1).fill(true), prime = [], queue = [];

for (let i=2; i<=SQRT_K; i++) {
    if (!isPrime[i]) continue;
    prime.push(i);
    for (let j = 2 * i; j <= SQRT_K; j += i)
        isPrime[j] = false;
}

for (let i = 0; i < prime.length; i++) {
    let p = prime[i], len = queue.length;
    queue.push([p, 1]);
    for (let j=0; j<len; j++)
        if (p*queue[j][0] <= SQRT_K)
            queue.push([p*queue[j][0], -1*queue[j][1]]);
}

queue.sort((a, b) => (a[0] - b[0]));

function getRank(n) {
    let max_num = 0|Math.sqrt(n), retval = 0;
    for (let i=0; i<queue.length && queue[i][0]*queue[i][0] <= n; i++)
        retval += queue[i][1]*Math.floor(n / (queue[i][0] * queue[i][0]));
    return n - retval;
}

function search(k) {
    let s = 1, e = 2*k, m;
    while(s < e) {
        m = 0|(s + e)/2;
        if (k <= getRank(m)) e = m;
        else s = m + 1;
    }
    return e;
}

console.log(search(K));