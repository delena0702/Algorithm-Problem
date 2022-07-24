import sys
def input(): return sys.stdin.readline().strip()

def dfs(here):
    for there in edges[here]:
        if visited[there]:
            continue
        visited[there] = True

        if link[there] == -1 or dfs(link[there]):
            link[there] = here
            return 1
    return 0
        

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
    
    link = [-1 for _ in range(N)]
    answer = 0
    for i in range(N):
        visited = [False for _ in range(N)]
        answer = answer + dfs(i)
    print(answer)