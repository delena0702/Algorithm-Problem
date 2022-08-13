from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())

edges = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

queue = deque([(1, 0)])
visited = [False] * (N + 1)
visited[1] = True
answer = 0
while queue:
    here, depth = queue.popleft()

    check = True
    for there in edges[here]:
        if visited[there]:
            continue

        visited[there] = True
        queue.append((there, depth + 1))
        check = False
    if check:
        answer = answer + depth

print("Yes" if answer % 2 else "No")