let fs = require('fs');
let data = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(x => 0 | x);
var N = 9, sum = data.reduce((a, x) => a + x, 0);

function main() {
    for (let i = 0; i < N - 1; i++) {
        for (let j = i + 1; j < N; j++) {
            if (sum - data[i] - data[j] == 100) {
                data.splice(j, 1);
                data.splice(i, 1);
                data.sort((a, b) => (a - b));
                for (let n of data)
                    console.log(n);
                return;
            }
        }
    }
}

main();