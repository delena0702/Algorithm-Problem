from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

darr = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

N, M, K = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1

answer = 0
for idx in range(N * M):
    y, x = divmod(idx, M)
    x, y = x + 1, y + 1

    if arr[y][x] == 0:
        continue
    arr[y][x] = 0
    queue = deque([(x, y)])
    size = 0
    while queue:
        x, y = queue.popleft()
        size += 1

        for dx, dy in darr:
            nx, ny = x + dx, y + dy
            if not 0 < nx <= M:
                continue
            if not 0 < ny <= N:
                continue
            if arr[ny][nx] == 0:
                continue
            arr[ny][nx] = 0
            queue.append((nx, ny))

    answer = max(answer, size)
print(answer)