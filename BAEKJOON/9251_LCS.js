let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [a, b] = input, NA = a.length, NB = b.length;
let dp = new Array(NA + 1);
for (let i = 0; i <= NA; i++)
    dp[i] = new Array(NB + 1).fill(0);

for (let i = NA - 1; i >= 0; i--)
    for (let j = NB - 1; j >= 0; j--)
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1], (a[i] == b[j]) ? (dp[i + 1][j + 1] + 1) : 0);
console.log(dp[0][0]);