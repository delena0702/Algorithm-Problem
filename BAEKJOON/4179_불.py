from cmath import isinf
import sys
import math
from collections import deque
def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]


jx, jy, fire = -1, -1, []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J':
            jx, jy = j, i
        elif arr[i][j] == 'F':
            fire.append((j, i))


fire_dp = [[float('inf')] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
queue = deque(list(map(lambda x: (x[0], x[1], 0), fire)))

while queue:
    x, y, distance = queue.popleft()

    fire_dp[y][x] = distance

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if arr[ny][nx] == '#':
            continue
        if not math.isinf(fire_dp[ny][nx]):
            continue

        fire_dp[ny][nx] = distance + 1
        queue.append((nx, ny, distance + 1))

answer = -1
queue = deque([(jx, jy, 0)])
visited = [[False] * M for _ in range(N)]
visited[jy][jx] = True
while(queue):
    x, y, distance = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            answer = distance + 1
            break
        if visited[ny][nx]:
            continue
        if arr[ny][nx] == '#':
            continue
        if fire_dp[ny][nx] <= distance + 1:
            continue

        visited[ny][nx] = True
        queue.append((nx, ny, distance + 1))

    if answer != -1:
        break

print(answer if answer != -1 else "IMPOSSIBLE")