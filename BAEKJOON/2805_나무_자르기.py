import sys
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
data = list(map(int, input().split()))
l, r = 0, max(data)
while (l < r):
    m = (l + r) // 2
    if sum(map(lambda x: max(x - m, 0), data)) >= M:
        l = m + 1
    else:
        r = m
print(r - 1)