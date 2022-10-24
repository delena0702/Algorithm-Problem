import sys
def input(): return sys.stdin.readline().strip()

darr = {
    "U": (0, -1, 2),
    "D": (0, 1, 2),
    "L": (-1, 0, 1),
    "R": (1, 0, 1),
}

N = int(input())
arr = [[0] * N for _ in range(N)]

ops = input()
x, y = 0, 0
for op in ops:
    dx, dy, t = darr[op]
    nx, ny = x + dx, y + dy

    if not 0 <= nx < N:
        continue
    if not 0 <= ny < N:
        continue

    arr[y][x] |= t
    arr[ny][nx] |= t

    x, y = nx, ny

chs = ['.', '-', '|', '+']
for i in range(N):
    for j in range(N):
        print(chs[arr[i][j]], end='')
    print()
