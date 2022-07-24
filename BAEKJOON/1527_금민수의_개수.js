var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
var A = 0|input[0], B = 0|input[1];
console.log(_dfs(4) + _dfs(7));

function  _dfs(n) {
    if (n > B) return 0;
    return ((n >= A && n <= B) ? 1 : 0) + _dfs(10*n + 4) + _dfs(10*n + 7);
}