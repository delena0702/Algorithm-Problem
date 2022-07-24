import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
data = []
for _ in range(N):
    data.append(input())

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
queue = deque([(0, 0, 1)])
visited = [[False] * M for _ in range(N)]
answer = 0
while queue:
    (x, y, d) = queue.popleft()

    if x == M - 1 and y == N - 1:
        answer = d
        break

    if x < 0 or x >= M or y < 0 or y >= N:
        continue
    if visited[y][x]:
        continue
    if data[y][x] == '0':
        continue
    visited[y][x] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        queue.append((nx, ny, d + 1))

print(d)
