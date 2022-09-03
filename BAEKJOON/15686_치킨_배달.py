from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = [input().split() for _ in range(N)]
homes, chickens = [], []
for i in range(N):
    for j in range(N):
        if data[i][j] == '1':
            homes.append((j, i))
        elif data[i][j] == '2':
            chickens.append((j, i))

answer = float('inf')
for arr in combinations(chickens, M):
    length = 0
    for hx, hy in homes:
        l = float('inf')
        for cx, cy in arr:
            l = min(l, abs(cx - hx) + abs(cy - hy))
        length = length + l
    answer = min(answer, length)
print(answer)