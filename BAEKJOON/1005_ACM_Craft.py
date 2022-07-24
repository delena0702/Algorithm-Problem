import sys
def input(): return sys.stdin.readline().strip()


def dfs(here):
    if distance[here] != -1:
        return distance[here]

    retval = 0
    for there in edges[here]:
        retval = max(retval, dfs(there))
    distance[here] = retval + D[here]
    return distance[here]


T = int(input())
while T:
    T -= 1

    (N, K) = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    edges = [[] for i in range(N+1)]

    for _ in range(K):
        (b, a) = map(int, input().split())
        edges[a].append(b)
    W = int(input())

    distance = [-1] * (N+1)
    print(dfs(W))
