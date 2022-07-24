import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

T = int(input())
while T:
    T -= 1

    (M, N, K) = map(int, input().split())
    data = [[0]*M for i in range(N)]
    for _ in range(K):
        (x, y) = map(int, input().split())
        data[y][x] = 1

    answer = 0
    for index in range(N*M):
        (y, x) = divmod(index, M)
        if data[y][x] != 1:
            continue
        queue = deque([(x, y)])
        while queue:
            (x, y) = queue.popleft()

            if x < 0 or x >= M or y < 0 or y >= N:
                continue
            if data[y][x] != 1:
                continue

            data[y][x] = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                queue.append((nx, ny))
        answer += 1
    print(answer)
