import sys
import heapq

(N, M, K) = map(int, sys.stdin.readline().strip().split())

edges = [[] for _ in range(N + 1)]

for i in range(M):
    (a, b, c) = map(int, sys.stdin.readline().strip().split())
    edges[a].append((b, c))

pq = [(0, 1)]
total_distance = [[0, 0] for _ in range(N+1)]
while pq:
    (distance, here) = heapq.heappop(pq)
    if total_distance[here][1] == K:
        continue

    total_distance[here][1] += 1
    total_distance[here][0] = distance

    for (there, d) in edges[here]:
        heapq.heappush(pq, (distance + d, there))
for answer in total_distance[1:]:
    print(answer[0] if answer[1] == K else -1)
