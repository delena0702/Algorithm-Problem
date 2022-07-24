from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

def dfs(here):
    if visited[here]:
        return
    visited[here] = True

    print(here, end=' ')

    for there in range(1, N + 1):
        if not graph[here][there]:
            continue
        dfs(there)


N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1)
visited[V] = True
queue = deque([V])
while queue:
    here = queue.popleft()
    print(here, end=' ')

    for there in range(1, N + 1):
        if not graph[here][there]:
            continue
        if visited[there]:
            continue
        visited[there] = True
        queue.append(there)
print()