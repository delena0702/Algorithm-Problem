import sys
INF = 987654321
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())

edges = [[INF] * (N + 1) for _ in range(N + 1)]
route = [[i] * (N + 1) for i in range(N + 1)]

for _ in range(M):
    (a, b, w) = map(int, input().split())
    edges[a][b] = w
    edges[b][a] = w
    route[a][b] = b
    route[b][a] = a

for i in range(1, N + 1):
    edges[i][i] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if edges[j][k] > edges[j][i] + edges[i][k]:
                edges[j][k] = edges[j][i] + edges[i][k]
                route[j][k] = route[j][i]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(route[i][j] if i != j else '-', end=' ')
    print()
