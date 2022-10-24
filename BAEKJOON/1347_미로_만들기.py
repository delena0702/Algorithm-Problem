import sys
def input(): return sys.stdin.readline().strip()

darr = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

N = int(input())
order = input()
data = [[False] * 100 for _ in range(100)]
x, y, d = 50, 50, 2
xl, xh, yl, yh = 50, 50, 50, 50

for ch in order:
    data[y][x] = True

    if ch == 'L':
        d = (d + 3) % 4
        continue

    if ch == 'R':
        d = (d + 1) % 4
        continue

    dx, dy = darr[d]
    x, y = x + dx, y + dy

    xl = min(xl, x)
    xh = max(xh, x)
    yl = min(yl, y)
    yh = max(yh, y)
data[y][x] = True

for i in range(yl, yh + 1):
    for j in range(xl, xh + 1):
        print('.' if data[i][j] else'#', end='')
    print()