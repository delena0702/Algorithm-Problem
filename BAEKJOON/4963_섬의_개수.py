from collections import deque
import sys
sys.stdin = open("1.txt")
def input(): return sys.stdin.readline().strip()

d = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    data = [list(map(int, input().split())) for _ in range(H)]
    answer = 0
    for i in range(W * H):
        sy, sx = divmod(i, W)
        if not data[sy][sx]:
            continue

        queue = deque([(sx, sy)])
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if not 0 <= nx < W or not 0 <= ny < H:
                    continue
                if not data[ny][nx]:
                    continue

                data[ny][nx] = 0
                queue.append((nx, ny))

        answer = answer + 1
    
    print(answer)
