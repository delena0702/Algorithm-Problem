from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N, M = int(input()), int(input())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (N + 1)
visited[1] = True
queue, answer = deque([1]), -1
while queue:
    here, answer = queue.popleft(), answer + 1
    for there in edges[here]:
        if visited[there]:
            continue
        visited[there] = True
        queue.append(there)
print(answer)
