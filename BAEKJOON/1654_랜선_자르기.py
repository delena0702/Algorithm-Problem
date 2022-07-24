import sys
def input(): return sys.stdin.readline().strip()

K, N = map(int, input().split())
data = [int(input()) for i in range(K)]

def canSolve(length):
    cnt = 0
    for l in data:
        cnt = cnt + l // length
    return cnt >= N

s, e = 1, max(data) + 1
while s < e:
    m = (s + e) // 2
    if canSolve(m):
        s = m + 1
    else:
        e = m
print(s - 1)