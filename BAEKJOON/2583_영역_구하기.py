from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

darr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

M, N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(K)]
board = [[False] * N for _ in range(M)]

for x1, y1, x2, y2 in data:
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = True

answer = []
for i in range(N * M):
    sy, sx = divmod(i, N)
    if board[sy][sx] == True:
        continue

    queue = deque([(sx, sy)])
    board[sy][sx] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in darr:
            nx, ny = x + dx, y + dy

            if not 0 <= nx < N or not 0 <= ny < M:
                continue
            if board[ny][nx]:
                continue

            board[ny][nx] = True
            cnt += 1
            queue.append((nx, ny))
    answer.append(cnt)

print(len(answer))
print(*sorted(answer))