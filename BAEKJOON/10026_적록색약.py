import sys
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def input(): return sys.stdin.readline().strip()


N = int(input())
data, answer = [input() for _ in range(N)], [0, 0]

for j in range(2):
    if j:
        data = [s.replace('G', 'R') for s in data]

    visited = [[False] * N for _ in range(N)]
    for ind in range(N * N):
        (y, x) = divmod(ind, N)
        if visited[y][x]:
            continue
        visited[y][x] = True
        answer[j] += 1

        color, queue = data[y][x], deque([(x, y)])
        while queue:
            (x, y) = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if visited[ny][nx]:
                    continue
                if color != data[ny][nx]:
                    continue
                visited[ny][nx] = True
                queue.append((nx, ny))

print(f"{answer[0]} {answer[1]}")