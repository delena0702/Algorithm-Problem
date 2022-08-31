from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
a, b = map(int, input().split())
M = int(input())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

queue = deque([(a, 0)])
visited = [False] * (N + 1)
visited[a] = True
while(queue):
    here, cost = queue.popleft()

    if here == b:
        print(cost)
        break

    for there in edges[here]:
        if visited[there]:
            continue

        visited[there] = True
        queue.append((there, cost + 1))
else:
    print(-1)