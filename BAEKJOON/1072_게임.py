from math import ceil

X, Y = map(int, input().split())
target = 100 * Y // X  + 1
if target >= 100:
    print(-1)
else:
    print(ceil((target * X - 100 * Y) / (100 - target)))