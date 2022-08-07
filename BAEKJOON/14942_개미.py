import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
nodes = [0] + [int(input()) for _ in range(N)]

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, weight = map(int, input().split())
    edges[a].append((b, weight))
    edges[b].append((a, weight))

answer = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(here, paths):
    visited[here] = True

    energy = nodes[here]
    for i in range(len(paths) - 1, -1, -1):
        _, cost = paths[i]
        energy -= cost

        if energy < 0:
            answer[here] = paths[i + 1][0] if i + 1 < len(paths) else here
            break
    else:
        answer[here] = 1

    for there, w in edges[here]:
        if visited[there]:
            continue
        
        paths.append((here, w))
        dfs(there, paths)
        paths.pop()

dfs(1, [])
print(*answer[1:], sep='\n')