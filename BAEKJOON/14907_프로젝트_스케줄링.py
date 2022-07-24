from collections import defaultdict
from heapq import heapify, heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

delay = {}
children = defaultdict(list)
pq = []
while True:
    arr = input().split()
    if not arr:
        break
    delay[arr[0]] = int(arr[1])
    if len(arr) == 3:
        for parent in arr[2]:
            children[parent].append(arr[0])
    else:
        pq.append((int(arr[1]), arr[0]))

heapify(pq)
dp = defaultdict(int)
answer = 0
while pq:
    cost, here = heappop(pq)
    answer = max(answer, cost)
    for there in children[here]:
        if cost + delay[there] <= dp[there]:
            continue
        dp[there] = cost + delay[there]
        heappush(pq, (dp[there], there))
print(answer)