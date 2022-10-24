from math import isinf
import sys
def input(): return sys.stdin.readline().strip()

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
for s, i, c in arr:
    if T < s:
        answer = min(answer, s - T)
        continue
    if T > s + i * (c - 1):
        continue
    temp = (s + i * (c - 1) - T) % i
    answer = min(answer, temp)
print(-1 if isinf(answer) else answer)