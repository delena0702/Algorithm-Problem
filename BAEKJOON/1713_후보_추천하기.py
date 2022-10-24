from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N, M = int(input()), int(input())
arr = list(map(int, input().split()))

answer = []
counter = defaultdict(int)
for i, num in enumerate(arr):
    counter[num] += 1

    if list(map(lambda x: x[1], answer)).count(num):
        continue

    if len(answer) < N:
        answer.append((i, num))
        continue
    
    min_idx = 0
    for j in range(1, N):
        idx, value = answer[j]
        if (counter[value], idx) < (counter[answer[min_idx][1]], answer[min_idx][0]):
            min_idx = j
    
    counter[answer[min_idx][1]] = 0
    answer[min_idx] = (i, num)

print(*sorted(map(lambda x: x[1], answer)))