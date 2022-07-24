from cmath import inf
from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


INF = 1234567
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
dp = [[[INF] * M for _ in range(N)] for _ in range(2)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque([(0, 0, False, 1)])
while len(queue):
    (x, y, isBroke, distance) = queue.popleft()

    if (distance >= dp[1 if isBroke else 0][y][x]):
        continue

    dp[1 if isBroke else 0][y][x] = distance

    for i in range(4):
        (nx, ny) = (x + dx[i], y + dy[i])

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if isBroke and data[ny][nx]:
            continue

        queue.append((nx, ny, True if data[ny][nx] else isBroke, distance + 1))

answer = min(dp[0][N-1][M-1], dp[1][N-1][M-1])
print(-1 if answer == INF else answer)
