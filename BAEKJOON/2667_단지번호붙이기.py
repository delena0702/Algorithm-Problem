from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

darr = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N = int(input())
data = [list(input()) for _ in range(N)]

answer = []
for i in range(N ** 2):
    sy, sx = divmod(i, N)
    if data[sy][sx] =='0':
        continue
    
    result = 0
    queue = deque([(sx, sy)])
    data[sy][sx] = '0'
    while queue:
        x, y = queue.popleft()
        result += 1

        for dx, dy in darr:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < N or not 0 <= ny < N:
                continue
            if data[ny][nx] == '0':
                continue
            data[ny][nx] = '0'
            queue.append((nx, ny))
    answer.append(result)
print(len(answer))
answer.sort()
print(*answer, sep='\n')