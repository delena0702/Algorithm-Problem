import sys
import heapq
def input(): return sys.stdin.readline().strip()


pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(pq, -x)
    else:
        print(-heapq.heappop(pq) if pq else 0)
