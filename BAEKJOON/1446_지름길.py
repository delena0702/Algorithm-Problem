from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

N, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

pos = set([0, D])
for a, b, c in arr:
    pos.add(a)
    pos.add(b)
pos = list(pos)
pos.sort()

index = {}
for i, num in enumerate(pos):
    index[num] = i

N = len(pos)
edges = [[] for _ in range(N)]

for i in range(N - 1):
    edges[i].append((i + 1, pos[i + 1] - pos[i]))

for a, b, c in arr:
    edges[index[a]].append((index[b], c))

dist = [float('inf')] * N
dist[0] = 0
pq = [(0, 0)]
while pq:
    distance, here = heappop(pq)
    for there, cost in edges[here]:
        if dist[there] <= dist[here] + cost:
            continue

        dist[there] = dist[here] + cost
        heappush(pq, (dist[there], there))
print(dist[index[D]])