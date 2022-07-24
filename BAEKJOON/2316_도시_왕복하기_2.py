import sys
from collections import deque
INF = 987654321
def input(): return sys.stdin.readline().strip()


(N, P) = map(int, input().split())
edges = [{} for _ in range(2*N)]
flow = [[0] * (2*N) for _ in range(2*N)]
for i in range(1, N):
    edges[2*i][2*i+1] = 1
    edges[2*i+1][2*i] = 0

for _ in range(P):
    (a, b) = map(int, input().split())
    a, b = a-1, b-1
    edges[2*a+1][2*b] = INF
    edges[2*b][2*a+1] = 0
    edges[2*b+1][2*a] = INF
    edges[2*a][2*b+1] = 0

answer = 0
while True:
    queue = deque([1])
    visited = [-1] * (2*N)
    visited[1] = 1
    while queue:
        if queue[0] == 2:
            break
        here = queue.popleft()
        for there in edges[here]:
            if edges[here][there] - flow[here][there] <= 0:
                continue
            if visited[there] != -1:
                continue
            visited[there] = here
            queue.append(there)

    if not queue:
        break
    answer += 1

    here = 2
    while here != 1:
        flow[visited[here]][here] += 1
        flow[here][visited[here]] -= 1
        here = visited[here]
print(answer)
