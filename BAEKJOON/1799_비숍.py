import sys
N = int(sys.stdin.readline().strip())

array = [0]*N
edges = [[] for _ in range(2*N-1)]
for i in range(N):
    array[i] = list(map(int, sys.stdin.readline().strip().split(' ')))
    for j in range(N):
        if array[i][j]:
            edges[j - i + N - 1].append(i + j)
matched = [-1]*(2*N-1)

def dfs(here):
    global visited
    if visited[here]:
        return 0
    visited[here] = True
    for there in edges[here]:
        if matched[there] == -1 or dfs(matched[there]):
            matched[there] = here
            return 1
    return 0

answer = 0
for i in range(2*N-1):
    visited = [False] * (2*N-1)
    answer += dfs(i)
print(answer)