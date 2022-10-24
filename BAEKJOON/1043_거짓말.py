from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
edges = [[] for _ in range(N + M + 1)]

_, *know = list(map(int, input().split()))

for i in range(1, M + 1):
    _, *arr = map(int, input().split())

    for j in arr:
        edges[N + i].append(j)
        edges[j].append(N + i)

queue = deque(know)
visited = [False] * (N + M + 1)
for here in know:
    visited[here] = True

while queue:
    here = queue.popleft()

    for there in edges[here]:
        if visited[there]:
            continue
        visited[there] = True
        queue.append(there)

print(visited[N + 1:].count(False))