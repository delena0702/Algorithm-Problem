from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i, x in enumerate(list(map(int, input().split()))):
    if x != -1:
        edges[i + 1].append(x)
        edges[x].append(i + 1)

nodes = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, input().split())
    nodes[i] = nodes[i] + w

visited = [False] * (N + 1)
visited[1] = True

queue = deque([(1, 0)])
while queue:
    here, cost = queue.popleft()
    nodes[here] = nodes[here] + cost

    for there in edges[here]:
        if visited[there]:
            continue

        visited[there] = True
        queue.append((there, nodes[here]))

print(*nodes[1:], sep=' ')
