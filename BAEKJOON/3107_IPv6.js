let input = require('fs').readFileSync('/dev/stdin').toString().trim();

while (input.split(':').length < 8)
    input = input.replace(/::/, ":::");
if (input.split(':').length  > 8) {
    input = input.replace(/^\:/, "");
    input = input.replace(/\:$/, "");
}

let data = input.split(':');
for (let i = 0; i < 8; i++)
    if (data[i].length < 4)
        data[i] = data[i].padStart(4, '0');
console.log(data.join(':'));