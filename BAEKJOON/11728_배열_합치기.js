let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [NA, NB] = input.shift().split(' ').map(x => 0 | x);
let data = input.map(x => {
    let ret = x.split(' ').map(x => 0 | x);
    ret.push(Infinity);
    return ret;
});
let i = 0, j = 0, answer = [];

while (i < NA || j < NB) {
    if (data[0][i] < data[1][j])
        answer.push(data[0][i++]);
    else
        answer.push(data[1][j++]);
}

console.log(answer.join(' '));