let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
input.shift();
var data = input.map(x => x.split(' ')[1] - x.split(' ')[0]);

for (let x of data) {
    let k = Math.ceil(Math.sqrt(x));
    if (x <= k * (k - 1)) console.log(2 * k - 2);
    else console.log(2 * k - 1);
}