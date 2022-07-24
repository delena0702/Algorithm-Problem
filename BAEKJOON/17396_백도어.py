import sys
import heapq
INF = 98765432100
def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split())

data = list(map(int, input().split()))
data[N-1] = 0

edges = [[] for _ in range(N)]
for _ in range(M):
    (a, b, w) = map(int, input().split())
    if data[a] == 0 and data[b] == 0:
        edges[a].append((b, w))
        edges[b].append((a, w))

# dijkstra
pq = [(0, 0)]
dijkstra = [INF] * N
while pq:
    (distance, here) = heapq.heappop(pq)
    if dijkstra[here] <= distance:
        continue
    dijkstra[here] = distance
    if here == N-1:
        break

    for (there, weight) in edges[here]:
        heapq.heappush(pq, (distance + weight, there))
print(dijkstra[-1] if dijkstra[-1] != INF else -1)
