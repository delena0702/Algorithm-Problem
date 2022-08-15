from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


N, M, X = map(int, input().split())

edges = [[[] for _ in range(N + 1)] for _ in range(2)]
for i in range(M):
    a, b = map(int, input().split())
    edges[0][b].append(a)
    edges[1][a].append(b)

for i in range(2):
    queue = deque([X])
    visited = [False] * (N + 1)
    visited[X] = True

    cnt = 0
    while queue:
        here = queue.popleft()
        for there in edges[i][here]:
            if visited[there]:
                continue

            visited[there] = True
            cnt = cnt + 1
            queue.append(there)

    if i == 0:
        print(cnt + 1, end=' ')
    else:
        print(N - cnt)
