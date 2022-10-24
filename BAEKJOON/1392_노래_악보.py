import sys
def input(): return sys.stdin.readline().strip()

N, Q = map(int, input().split())
data = [0] + [int(input()) for _ in range(N)]
psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + data[i]

for _ in range(Q):
    num = int(input())
    s, e = 0, N + 1
    while s < e:
        m = (s + e) // 2
        if num < psum[m]:
            e = m
        else:
            s = m + 1
    print(s)