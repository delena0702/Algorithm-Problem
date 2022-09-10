from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
pq = []
for i in range(N):
    x = int(input())
    if x:
        heappush(pq, (abs(x), x))
    else:
        if pq:
            print(heappop(pq)[1])
        else:
            print(0)