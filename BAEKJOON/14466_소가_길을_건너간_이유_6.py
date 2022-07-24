from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()
def encode(r, c): return (r - 1) * N + (c - 1)


N, K, R = map(int, input().split())

edges = [[] for _ in range(N * N)]
for i in range(1, N + 1):
    for j in range(1, N):
        edges[encode(i, j)].append(encode(i, j + 1))
        edges[encode(i, j + 1)].append(encode(i, j))
        edges[encode(j, i)].append(encode(j + 1, i))
        edges[encode(j + 1, i)].append(encode(j, i))

for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    a, b = encode(r1, c1), encode(r2, c2)
    edges[a].pop(edges[a].index(b))
    edges[b].pop(edges[b].index(a))

nodes = [-1] * (N * N)
cows = [0] * K
for i in range(K):
    cows[i] = encode(*map(int, input().split()))

for i in range(K):
    if nodes[cows[i]] != -1:
        continue

    queue = deque([cows[i]])
    value = cows[i]
    nodes[cows[i]] = value

    while queue:
        here = queue.popleft()

        for there in edges[here]:

            if nodes[there] != -1:
                continue

            nodes[there] = value
            queue.append(there)

answer = 0
for a, b in combinations(cows, 2):
    if nodes[a] != nodes[b]:
        answer = answer + 1

print(answer)
