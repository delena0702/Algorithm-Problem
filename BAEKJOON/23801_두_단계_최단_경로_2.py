import sys
import heapq
INF = float('inf')
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    (u, v, w) = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

(X, Z) = map(int, input().split())
input()
Y = set(map(int, input().split()))

dijkstra, queue = [[INF] * (N + 1) for _ in range(2)], [(0, X, False)]

while queue:
    (distance, here, isPassed) = heapq.heappop(queue)

    if dijkstra[isPassed][here] <= distance:
        continue

    dijkstra[isPassed][here] = distance
    dijkstra[0][here] = distance

    if isPassed and here == Z:
        break

    isPassed = isPassed or here in Y
    for (there, weight) in edges[here]:
        heapq.heappush(queue, (distance + weight, there, isPassed))

print(dijkstra[1][Z] if dijkstra[1][Z] != INF else -1)
