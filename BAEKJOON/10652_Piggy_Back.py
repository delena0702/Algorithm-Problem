from collections import deque
from math import isinf
import sys
def input(): return sys.stdin.readline().strip()


def bfs(start, index):
    queue = deque([(start, 0)])
    distances[start][index] = 0

    while queue:
        here, d = queue.popleft()

        for there in graph[here]:
            if not isinf(distances[there][index]):
                continue
            distances[there][index] = d + 1

            queue.append((there, d + 1))


B, E, P, N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distances = [[float('inf')] * (3) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1, 0)
bfs(2, 1)
bfs(N, 2)

print(min(map(lambda x: B * x[0] + E * x[1] + P * x[2], distances)))
