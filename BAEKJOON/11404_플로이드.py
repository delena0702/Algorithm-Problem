from math import isinf
import sys
def input(): return sys.stdin.readline().strip()

N, M = int(input()), int(input())
edges = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    edges[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a - 1][b - 1] = min(edges[a - 1][b - 1], c)

for i in range(N):
    for j in range(N):
        for k in range(N):
            edges[j][k] = min(edges[j][k], edges[j][i] + edges[i][k])

for arr in edges:
    print(*map(lambda x: 0 if isinf(x) else x, arr), sep=' ')