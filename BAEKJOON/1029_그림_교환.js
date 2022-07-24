var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
let N = 0|input.shift(), data = new Array(N), dp = {};

for (let i=0; i<N; i++)
    data[i] = input.shift().split('').map(x => 0 | x);

function _dfs(start, price, visited) {
    if (visited & (1 << start)) return 0;
    visited = visited | (1 << start);

    if (dp[(start * 10 + price) * (1 << N) + visited] !== undefined)
        return dp[(start * 10 + price) * (1 << N) + visited];

    let retval = 0;
    for (let i=0; i<N; i++)
        if (data[start][i] >= price)
            retval = Math.max(_dfs(i, data[start][i], visited), retval);

    dp[(start * 10 + price) * (1 << N) + visited] = retval + 1;

    return retval + 1;
}

console.log(_dfs(0, 0, 0));