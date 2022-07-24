var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
let N = 0|input.shift(), data = new Array(N);

for (let i=0; i<N; i++) {
    input.shift();
    data[i] = input.shift();
}

for (let str of data) {
    let end = {}, cnt = {}, res = {}, subSum = -1, answer = 0;

    for (let i = 0; i < str.length; i++) {
        let ch = str[i];
        end[ch] = i;
        cnt[ch] = cnt[ch] + 1 || 1;
    }

    let rank = Object.keys(end);
    rank.sort((a, b) => (end[a] - end[b]));

    for (let ch of rank) {
        subSum += cnt[ch];
        res[ch] = subSum;
    }

    for (let ch in end)
        answer += (end[ch] - res[ch]) * 5 * cnt[ch];

    console.log(answer);
}