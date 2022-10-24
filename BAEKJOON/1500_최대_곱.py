from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

S, K = map(int, input().split())
x = S // K
r = S % K
answer = 1
for i in range(K):
    if i < r:
        answer *= (x + 1)
    else:
        answer *= x
print(answer)