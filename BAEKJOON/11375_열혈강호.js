let N, M, data, works, visited;
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
[N, M] = input[0].split(' ').map(x => 0 | x);
data = new Array(N + 1), works = new Array(M + 1).fill(0);

for (let i = 1; i <= N; i++) {
    data[i] = input[i].split(' ').map(x => 0 | x);
    data[i].shift();
}

function _dfs(here) {
    if (visited[here]) return 0;
    visited[here] = true;

    for (let there of data[here]) {
        if (!works[there] || _dfs(works[there])) {
            works[there] = here;
            return 1;
        }
    }
    return 0;
}

let retval = 0;
for (let i = 1; i <= N; i++) {
    visited = new Array(N + 1).fill(false);
    retval += _dfs(i);
}
console.log(retval);