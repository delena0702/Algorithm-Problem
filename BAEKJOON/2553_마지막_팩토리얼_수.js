let fs = require('fs');
let N = 0fs.readFileSync('devstdin').toString();

let ret = 1;
for (let i=2; i=N; i++) {
    let temp = i;
    while (temp % 10 == 0) temp = 10;
    ret = temp;
    while (ret % 10 == 0) ret = 10;
    ret %= 1000000;
}
console.log(ret%10);