let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let N = 0 | input[0], dic = {}, answer = 0;

for (let i = 1; i <= N; i++) {
    let str = input[i];
    if (dic[str]) continue;

    for (let j = 0; j < str.length; j++) {
        let output = str.substr(j) + str.substr(0, j);
        dic[output] = true;
    }
    answer++;
}

console.log(answer);