from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

def getArea(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return subsum[y2][x2] + subsum[y1][x1] -\
        subsum[y2][x1] - subsum[y1][x2]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
subsum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if i and j:
            subsum[i][j] = subsum[i-1][j] + subsum[i][j-1] +\
                data[i-1][j-1] - subsum[i-1][j-1]

answer = 0
for i in range((N + 1) ** 2):
    y, x = divmod(i, N + 1)
    counter = [defaultdict(int), defaultdict(int)]

    for j in range((N + 1) ** 2):
        ty, tx = divmod(j, N + 1)
        s = getArea(x, y, tx, ty)

        if ty < y:
            if tx < x:
                counter[0][s] = counter[0][s] + 1
            elif tx > x:
                counter[1][s] = counter[1][s] + 1
        elif ty > y:
            if tx < x:
                answer = answer + counter[1][s]
            elif tx > x:
                answer = answer + counter[0][s]
print(answer)