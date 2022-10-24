from re import L
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
s = set(map(int, input().split()))

answer = float('inf')
for i in range(1, 1002):
    if i in s:
        continue
    for j in range(i, 1002):
        if j in s:
            continue
        for k in range(j, 1002):
            if k in s:
                continue
            answer = min(answer, abs(N - i * j * k))
print(answer)
