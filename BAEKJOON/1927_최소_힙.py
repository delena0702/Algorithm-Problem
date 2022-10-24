from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
pq = []
for _ in range(N):
    num = int(input())
    if num:
        heappush(pq, num)
    else:
        if pq:
            print(heappop(pq))
        else:
            print(0)