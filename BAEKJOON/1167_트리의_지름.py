from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    retval = (-1, 0)
    while queue:
        here, distance = queue.popleft()
        if distance > retval[0]:
            retval = (distance, here)

        for there, cost in edges[here]:
            if visited[there]:
                continue
            visited[there] = True
            queue.append((there, distance + cost))

    return retval

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(1, N + 1):
    i, *arr = map(int, input().split())
    for j in range(len(arr) // 2):
        edges[i].append((arr[2 * j], arr[2 * j + 1]))

_, s = bfs(1)
answer, _ = bfs(s)
print(answer)