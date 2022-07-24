import sys
T = int(sys.stdin.readline().strip())

while T > 0:
    T -= 1
    (x1, y1, r1, x2, y2, r2) = map(int, sys.stdin.readline().strip().split())
    d = (x1-x2)**2 + (y1-y2)**2
    rm = (r1 - r2)**2
    rM = (r1 + r2)**2

    if d == 0 and rm == 0:
        print(-1)
    elif d < rm or rM < d:
        print(0)
    elif d == rm or d == rM:
        print(1)
    else:
        print(2)
