import sys
def input(): return sys.stdin.readline().strip()

N, C, W = map(int, input().split())
data = [int(input()) for _ in range(N)]

answer = -float('inf')
for i in range(1, 10001):
    t1 = 0
    for j in range(N):
        if data[j] // i == 0:
            continue
        t2 = 0
        t2 += data[j] // i * i * W
        t2 -= (data[j] - 1) // i * C
        if t2 > 0:
            t1 += t2
    answer = max(answer, t1)
print(answer)