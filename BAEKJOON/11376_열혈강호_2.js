let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let N, M, works, data, visited;
[N, M] = input[0].split(' ').map(x => 0 | x);
works = new Array(M + 1).fill(0), data = new Array(N + 1);

for (let i = 1; i <= N; i++) {
    data[i] = input[i].split(' ').map(x => 0 | x);
    data[i].shift();
}

let answer = 0;
for (let i = 1; i <= 2*N; i++) {
    visited = new Array(2 * N + 1).fill(false);
    if (_dfs(i)) answer++;
}
console.log(answer);

function _dfs(here) {
    if (visited[here]) return false;
    visited[here] = true;

    for (let there of data[0|(here+1)/2]) {
        if (!works[there] || _dfs(works[there])) {
            works[there] = here;
            return true;
        }
    }
    return false;
}