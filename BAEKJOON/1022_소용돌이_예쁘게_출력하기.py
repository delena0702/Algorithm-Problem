import sys
def input(): return sys.stdin.readline().strip()

arr = list(map(int, input().split()))
r1, c1, r2, c2 = arr
s = min(list(map(abs, arr)))
if r1 * r2 < 0 or c1 * c2 < 0:
    s = 0
e = max(list(map(abs, arr)))
answer = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

def check(x, y, n):
    if not c1 <= x <= c2:
        return
    if not r1 <= y <= r2:
        return
    answer[y - r1][x - c1] = n

cnt = (2 * s - 1) ** 2 + 1 if s else 1
for i in range(s, e + 1):
    if i == 0:
        check(0, 0, cnt)
        cnt += 1
        continue

    for j in range(i - 1, -i, -1):
        check(i, j, cnt)
        cnt += 1
    for k in range(i, -i - 1, -1):
        check(k, -i, cnt)
        cnt += 1
    for j in range(-i + 1, i):
        check(-i, j, cnt)
        cnt += 1
    for k in range(-i, i + 1):
        check(k, i, cnt)
        cnt += 1

l = 0
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        l = max(l, len(str(answer[i][j])))

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(answer[i][j]).rjust(l, ' '), end=' ')
    print()