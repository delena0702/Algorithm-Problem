from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def getNext(x, y, distance):
    retval = []
    for i in range(4):
        nx, ny, cost, check = x, y, 0, False
        while True:
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                break
            if data[ny][nx] == 'R':
                nx, ny = nx - dx[i], ny - dy[i]
                cost = cost - int(data[ny][nx])
                check = True
                break
            if data[ny][nx] == 'E':
                check = True
                break
            if data[ny][nx] == 'H':
                break

            cost = cost + int(data[ny][nx])
            nx, ny = nx + dx[i], ny + dy[i]
        
        if not check:
            continue

        retval.append((nx, ny, distance + cost))
    return retval

W, H = map(int, input().split())
data = [list(input()) for _ in range(H)]
sx, sy = -1, -1

check = False
for i in range(H):
    for j in range(W):
        if data[i][j] == 'T':
            sx, sy = j, i
            data[i][j] = '0'
            check = True
            break
    if check:
        break

dp = [[float('inf')] * W for _ in range(H)]
queue = [(0, sx, sy)]
dp[sy][sx] = 0
while queue:
    distance, x, y = heappop(queue)

    if data[y][x] == 'E':
        print(distance)
        break

    if dp[y][x] < distance:
        continue

    for nx, ny, d in getNext(x, y, distance):
        if dp[ny][nx] <= d:
            continue
        dp[ny][nx] = d
        heappush(queue, (d, nx, ny))
else:
    print(-1)