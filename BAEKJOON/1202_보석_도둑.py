from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = []
for _ in range(N):
    m, v = map(int, input().split())
    arr.append((m, v))
arr.sort()

bags = [int(input()) for _ in range(K)]
bags.sort()

answer = 0
pq = []
idx = 0
for bag in bags:
    while idx < N:
        if arr[idx][0] > bag:
            break

        heappush(pq, -arr[idx][1])
        idx += 1
    if pq:
        answer += -heappop(pq)
print(answer)