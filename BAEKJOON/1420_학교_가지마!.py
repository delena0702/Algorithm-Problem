import sys
from collections import deque
INF = 987654321
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
data = []
for i in range(N):
    data.append(input())
    for (j, ch) in enumerate(data[i]):
        if data[i][j] == 'K':
            start = M*i+j + N*M
        if data[i][j] == 'H':
            end = M*i+j

capacity = [{} for _ in range(2*N*M)]
flow = [{} for _ in range(2*N*M)]
for i in range(N*M):
    (y, x) = divmod(i, M)

    if data[y][x] != '#':
        if i != start:
            capacity[i][i + N*M] = 1
            capacity[i + N*M][i] = 0

        if x+1 < M and data[y][x+1] != '#':
            capacity[i + N*M][M*(y)+(x+1)] = INF
            capacity[M*(y)+(x+1)][i + N*M] = 0
            capacity[M*(y)+(x+1) + N*M][i] = INF
            capacity[i][M*(y)+(x+1) + N*M] = 0

        if y+1 < N and data[y+1][x] != '#':
            capacity[i + N*M][M*(y+1)+(x)] = INF
            capacity[M*(y+1)+(x)][i + N*M] = 0
            capacity[M*(y+1)+(x) + N*M][i] = INF
            capacity[i][M*(y+1)+(x) + N*M] = 0

answer = 0
while True:
    queue = deque([start])
    visited = [-1]*(2*N*M)
    while queue and queue[0] != end:
        here = queue.popleft()
        for (there, c) in capacity[here].items():
            if c - flow[here].get(there, 0) <= 0:
                continue
            if visited[there] != -1:
                continue
            visited[there] = here
            queue.append(there)
        pass

    if not queue:
        break
    if visited[end] == start:
        answer = -1
        break

    answer += 1

    here = end
    while here != start:
        flow[visited[here]][here] = flow[visited[here]].get(here, 0) + 1
        flow[here][visited[here]] = flow[here].get(visited[here], 0) - 1
        here = visited[here]

print(answer)
