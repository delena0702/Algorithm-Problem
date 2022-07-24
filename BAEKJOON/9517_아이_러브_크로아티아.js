let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let now = 0 | input.shift(), N = 0 | input.shift(), time = 0;

for (let i = 0; i < N; i++) {
    let [t, ans] = input.shift().split(' ');
    time += 0 | t;
    if (time >= 210) break;
    if (ans == 'T') now = now % 8 + 1;
}

console.log(now);