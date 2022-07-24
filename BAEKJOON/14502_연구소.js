let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, M] = input.shift().split(' ').map(x => 0|x);
let data = input.map(x => x.split(' ').map(x => 0 | x));
const dir_data = [[0, -1], [1, 0], [0, 1], [-1, 0]];

console.log(makeWall(3, 0));

function makeWall(cnt, start_ind) {
    if (cnt == 0) {
        let temp_data = data.map(x=>x.map(x=>x));
        infect();
        let retval = data.reduce((a, x) => a + x.filter((x) => x == 0).length, 0);
        data = temp_data;
        return retval;
    }

    let retval = 0;
    for (let i = start_ind; i < N * M; i++) {
        let x = i % M, y = 0 | i / M;

        if (data[y][x] == 0) {
            data[y][x] = 1;
            retval = Math.max(retval, makeWall(cnt - 1, i + 1));
            data[y][x] = 0;
        }
    }
    return retval;
}

function infect() {
    let queue = [];

    for (let i=0; i<N; i++)
        for (let j=0; j<M; j++)
            if (data[i][j] == 2)
                queue.push([j, i]);
    
    while (queue.length) {
        let [x, y] = queue[0];
        queue.shift();

        for (let d of dir_data) {
            let nx = x + d[0], ny = y + d[1];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (data[ny][nx] == 0) {
                data[ny][nx] = 2;
                queue.push([nx, ny]);
            }
        }
    }
}