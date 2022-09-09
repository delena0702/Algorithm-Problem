from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

darr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for height in range(0, 102):
    check = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N ** 2):
        sy, sx = divmod(i, N)
        if check[sy][sx] or data[sy][sx] <= height:
            continue

        queue = deque([(sx, sy)])
        check[sy][sx] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in darr:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < N or not 0 <= ny < N:
                    continue
                if check[ny][nx] or data[ny][nx] <= height:
                    continue

                check[ny][nx] = True
                queue.append((nx, ny))
        cnt += 1
    answer = max(answer, cnt)
print(answer)