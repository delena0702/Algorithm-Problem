from collections import deque
from math import log2
import sys
def input(): return sys.stdin.readline().strip()


N = int(input())

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

ancestor = [[] for _ in range(N + 1)]
depth = [-1] * (N + 1)
depth[1] = 0
visited = [False] * (N + 1)
visited[1] = True

queue = deque([1])
while queue:
    here = queue.popleft()

    for there in edges[here]:
        if visited[there]:
            continue

        visited[there] = True
        depth[there] = depth[here] + 1
        ancestor[there].append(here)
        child, idx = here, 0
        while True:
            if len(ancestor[child]) <= idx:
                break

            ancestor[there].append(ancestor[child][idx])
            child = ancestor[child][idx]
            idx = idx + 1
        queue.append(there)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a

    d = depth[b] - depth[a]
    while d:
        b = ancestor[b][int(log2(-d & d))]
        d = d - (-d & d)

    while a != b:
        s, e = 0, len(ancestor[a])
        while s < e:
            m = (s + e) // 2
            if ancestor[a][m] == ancestor[b][m]:
                e = m
            else:
                s = m + 1

        a, b = ancestor[a][max(0, s - 1)], ancestor[b][max(0, s - 1)]
    print(a)
