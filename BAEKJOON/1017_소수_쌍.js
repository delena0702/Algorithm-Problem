let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const MAX = 2000;
let N = 0 | input[0];
let list = input[1].split(' ').map(x => 0 | x);
let temp_list, TN = 0|N/2-1, check, visited, isPrime = new Array(MAX);

for (let i=2; i<isPrime.length; i++) {
    if (isPrime[i] !== undefined) continue;
    for (let j = 1; i * j < isPrime.length; j++)
        isPrime[i*j] = (j == 1);
}

function main() {
    if (N%2) {
        console.log(-1);
        return;
    }

    let answer = [];
    for (let i=1; i<N; i++) {
        if (isPrime[list[0] + list[i]]) {
            let arr = list.slice(1,i).concat(list.slice(i+1));
            
            temp_list = [[], []];
            for (let num of arr)
                temp_list[num%2].push(num);
            
            check = new Array(TN).fill(-1);
            let check_end = true;
            for (let i=0; check_end && i<TN; i++) {
                visited = new Array(TN);
                check_end = check_end && _dfs(i);
            }

            if (check_end) answer.push(list[i]);
        }
    }

    answer.sort((a, b) => (a - b));
    if (answer.length) console.log(answer.join(' '));
    else console.log(-1);
}

function _dfs(here) {
    if (visited[here]) return false;
    visited[here] = true;

    for (let i=0; i<TN; i++) {
        let val = temp_list[1][here] + temp_list[0][i];
        if (isPrime[val] && (check[i] == -1 || _dfs(check[i]))) {
            check[i] = here;
            return true;
        }
    }
    return false;
}

main();