from collections import defaultdict, deque
import sys
def input(): return sys.stdin.readline().strip()

darr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

M, N = map(int, input().split())
data = [list(input()) for _ in range(N)]
answer = defaultdict(int)

for i in range(N * M):
    y, x = divmod(i, M)
    if data[y][x] == '0':
        continue
    value = data[y][x]

    queue = deque([(x, y)])
    data[y][x] = '0'
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in darr:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M:
                continue
            if ny < 0 or ny >= N:
                continue
            if data[ny][nx] != value:
                continue

            data[ny][nx] = '0'
            queue.append((nx, ny))

    answer[value] += cnt ** 2
print(answer['W'], answer['B'])