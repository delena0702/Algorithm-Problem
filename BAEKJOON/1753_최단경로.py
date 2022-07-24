import sys
import heapq
(V, E) = map(int, sys.stdin.readline().strip().split())
start = int(sys.stdin.readline().strip())
edges = [[] for i in range(V+1)]
INF = 987654321

for i in range(E):
    (u, v, w) = map(int, sys.stdin.readline().strip().split())
    edges[u].append((v, w))

def dijkstra(start):
    distance = [INF]*(V + 1)
    pq = [(0, start)]
    cnt = 0
    while pq and cnt < V:
        (dis, here) = heapq.heappop(pq)
        if dis >= distance[here]:
            continue
        distance[here] = dis
        cnt += 1
        for (there, weight) in edges[here]:
            heapq.heappush(pq, (dis + weight, there))
    return distance

answer = dijkstra(start)[1:]
for val in answer:
    print(val if val != INF else "INF")