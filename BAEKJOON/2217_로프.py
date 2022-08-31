import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = list(sorted([int(input()) for _ in range(N)], reverse=True))
for i in range(N):
    data[i] = data[i] * (i + 1)
print(max(data))