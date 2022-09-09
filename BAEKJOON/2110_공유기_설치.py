import sys
def input(): return sys.stdin.readline().strip()

N, C = map(int, input().split())
data = [int(input()) for _ in range(N)]
data.sort()
s, e = 1, (data[-1] - data[0]) // (C - 1) + 1

while s < e:
    m = (s + e) // 2
    check = False
    idx, cnt = data[0], 1
    for num in data:
        if num - idx >= m:
            idx, cnt = num, cnt + 1

    if cnt >= C:
        s = m + 1
    else:
        e = m
print(e - 1)