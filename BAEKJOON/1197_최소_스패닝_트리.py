from heapq import heappop, heappush
import sys
def input(): return sys.stdin.readline().strip()

V, E = map(int, input().split())

edges = [[] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a - 1].append((b - 1, c))
    edges[b - 1].append((a - 1, c))

pq = [(0, 0)]
solved = [False] * (V + 1)
answer = 0
for _ in range(V):
    while True:
        weight, here = heappop(pq)
        if not solved[here]:
            break

    solved[here] = True
    answer = answer + weight

    for there, w in edges[here]:
        if solved[there]:
            continue

        heappush(pq, (w, there))
print(answer)