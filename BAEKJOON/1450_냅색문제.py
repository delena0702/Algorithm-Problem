import sys
from itertools import combinations
def input(): return sys.stdin.readline().strip()


N, C = map(int, input().split())
data = sorted(list(map(int, input().split())))

left, right = data[:N//2], data[N//2:]
left_subset, right_subset = [], []

for i in range(0, len(left) + 1):
    for combination in combinations(left, i):
        left_subset.append(sum(combination))

for i in range(0, len(right) + 1):
    for combination in combinations(right, i):
        right_subset.append(sum(combination))

left_subset.sort()
right_subset.sort()

answer = 0
for value in right_subset:
    lo, hi = 0, len(left_subset)
    while lo < hi:
        mi = (lo + hi) // 2
        if left_subset[mi] + value > C:
            hi = mi
        else:
            lo = mi + 1

    if lo == 0:
        break
    answer = answer + lo

print(answer)
