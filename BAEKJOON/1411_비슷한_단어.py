from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [input() for _ in range(N)]

answer = 0
for a, b in combinations(range(N), 2):
    check = {}

    for i in range(len(data[0])):
        if data[a][i] in check:
            if check[data[a][i]] != data[b][i]:
                break
            continue
        check[data[a][i]] = data[b][i]
    else:
        if len(set(check.values())) == len(check):
            answer += 1
print(answer)