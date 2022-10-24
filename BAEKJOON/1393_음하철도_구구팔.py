import sys
def input(): return sys.stdin.readline().strip()

sx, sy = map(int,input().split())
ex, ey, dx, dy = map(int, input().split())

if dx == 0 and dy == 0:
    x, y = ex, ey
else:
    p = max(0, (sx - ex) * dx + (sy - ey) * dy)
    x = ex + dx * p // (dx ** 2 + dy ** 2)
    y = ey + dy * p // (dx ** 2 + dy ** 2)
print(x, y)