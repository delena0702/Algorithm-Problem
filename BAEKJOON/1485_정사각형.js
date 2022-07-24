let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let T = 0 | input.shift();

for (let i = 0; i < T; i++) {
    let data = input.splice(input, 4).map(x => x.split(' ').map(x => 0 | x)), cnt = {}, check = false;

    for (let j = 0; !check && j < 3; j++) {
        for (let k = j + 1; !check && k < 4; k++) {
            let sum = (data[j][0] - data[k][0]) ** 2 + (data[j][1] - data[k][1]) ** 2;
            cnt[sum] = (0 | cnt[sum]) + 1;
            if (cnt[sum] == 4) check = true;
        }
    }

    console.log((check && Object.keys(cnt).length == 2) ? 1 : 0);
}