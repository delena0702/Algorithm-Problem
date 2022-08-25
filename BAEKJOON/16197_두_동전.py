from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 'o':
            coins.append((j, i))
            data[i][j] = '.'

answer, end_check = -1, False
check = set([(coins[0], coins[1])])
queue = deque([(0, [coins[0], coins[1]])])
while queue:
    cost, coin = queue.popleft()
    for i in range(4):
        ncoin, out = [0, 0], 0
        for j in range(2):
            ncoin[j] = (coin[j][0] + dx[i], coin[j][1] + dy[i])
            if not 0 <= ncoin[j][0] < M or not 0 <= ncoin[j][1] < N:
                out = out + 1
                continue
            if data[ncoin[j][1]][ncoin[j][0]] == '#':
                ncoin[j] = coin[j]

        if out == 0:
            if cost + 1 < 10 and (ncoin[0], ncoin[1]) not in check:
                queue.append((cost + 1, ncoin))
                check.add((ncoin[0], ncoin[1]))
        elif out == 1:
            answer, end_check = cost + 1, True

    if end_check:
        break

print(answer)