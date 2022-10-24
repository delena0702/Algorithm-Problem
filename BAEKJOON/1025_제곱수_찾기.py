from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
answer = -1
for i in range(N * M):
    sy, sx = divmod(i, M)

    for j in range(N * M):
        if i == j:
            num = arr[sy][sx]
            if int(sqrt(num)) ** 2 == num:
                answer = max(answer, num)
            continue
        ny, nx = divmod(j, M)
        dx, dy = nx - sx, ny - sy
        x, y = sx, sy

        num = 0
        while True:
            if not 0 <= x < M:
                break
            if not 0 <= y < N:
                break
            
            num = 10 * num + arr[y][x]
            if int(sqrt(num)) ** 2 == num:
                answer = max(answer, num)
            x, y = x + dx, y + dy
            
print(answer)