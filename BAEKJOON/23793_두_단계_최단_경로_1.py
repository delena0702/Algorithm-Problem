import sys
import heapq
INF = float('inf')
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    (u, v, w) = map(int, input().split())
    edges[u].append((v, w))

(X, Y, Z) = map(int, input().split())

dijkstra, queue = [[INF] * (N + 1) for _ in range(2)], [(0, X, False)]

while queue:
    (distance, here, isPassed) = heapq.heappop(queue)
    isPassed = isPassed or here == Y

    if dijkstra[isPassed][here] <= distance:
        continue
    dijkstra[isPassed][here] = distance

    if dijkstra[0][Z] != INF and dijkstra[1][Z] != INF:
        break

    for (there, weight) in edges[here]:
        heapq.heappush(queue, (distance + weight, there, isPassed))

for i in range(1, -1, -1):
    print(dijkstra[i][Z] if dijkstra[i][Z] != INF else -1, end=' ')
