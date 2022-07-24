from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
for arr in combinations(data, 3):
    if sum(arr) <= M:
        answer = max(answer, sum(arr))
print(answer)