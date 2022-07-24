let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, M] = input.shift().split(' ').map(x => 0 | x);
let data = input.map(x => x.split('').map(x => 0 | x));
const dir_data = [[0, -1], [1, 0], [0, 1], [-1, 0]];

function bfs() {
    let queue = [[0, 0, 1, false]];
    let visited = {};

    while (queue.length) {
        let [x, y, dis, isBroken] = queue.shift();
        if (x < 0 || x >= M || y < 0 || y >= N) continue;
        if (x == M - 1 && y == N - 1) return dis;

        if ((isBroken ? 1 : 2) <= (0|visited[y * M + x])) continue;
        visited[y * M + x] = isBroken ? 1 : 2;

        if (isBroken && data[y][x]) continue;
        if (data[y][x]) isBroken = true;

        for (let d of dir_data)
            queue.push([x + d[0], y + d[1], dis + 1, isBroken]);
    }
    return -1;
}

console.log(bfs());