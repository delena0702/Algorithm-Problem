let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
let len = input.length, a = 0, b = 0;

for (let i = 0; i <= len - 3; i++) {
    if (input[i + 1] == 'O' && input[i + 2] == 'I') {
        switch (input[i]) {
            case 'J': a++; break;
            case 'I': b++; break;
        }
    }
}

console.log(a + "\n" + b);