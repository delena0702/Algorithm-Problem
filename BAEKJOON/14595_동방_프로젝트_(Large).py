import sys
def input(): return sys.stdin.readline().strip()

N, M = int(input()), int(input())

data = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    data[x - 1] = y - 1

answer, e = 0, 0
for i in range(N):
    e = max(e, data[i])
    if i == e:
        answer, e = answer + 1, e + 1

print(answer)