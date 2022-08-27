from collections import deque
import sys
sys.stdin = open("1.txt")
def input(): return sys.stdin.readline().strip()

d = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

T = int(input())
for _ in range(T):
    I = int(input())
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())

    data = [[float('inf')] * I for _ in range(I)]
    data[sy][sx] = 0
    queue = deque([(sx, sy)])
    check = True
    while queue and check:
        x, y = queue.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < I or not 0 <= ny < I:
                continue
            if data[ny][nx] <= data[y][x] + 1:
                continue

            data[ny][nx] = data[y][x] + 1
            if nx == fx and ny == fy:
                check = False
                break
            queue.append((nx, ny))

    print(data[fy][fx])