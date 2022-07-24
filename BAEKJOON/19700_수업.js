let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let N = 0 | input.shift();
let data = new Array(N), cnt = [];
for (let i = 0; i < N; i++)
    data[i] = input[i].split(' ').map(x => 0 | x);
data.sort((a, b) => (b[0] - a[0]));

for (let d of data) {
    let ind = search(d[1] - 1);
    if ( ind == cnt.length) cnt.push(1);
    else cnt[ind]++;
}
console.log(cnt.length);

function search(num) {
    let s = 0, e = cnt.length;
    while (s < e) {
        let m = 0 | (s + e) / 2;
        if (num >= cnt[m]) e = m;
        else s = m + 1;
    }
    return e;
}