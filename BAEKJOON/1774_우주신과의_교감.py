from heapq import heapify, heappop
from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()

def get(idx):
    here = idx
    while here != union[here]:
        here = union[here]
    root, here = here, idx
    while here != union[here]:
        here, union[here] = union[here], root
    return root

N, M = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(N)]

union = [i for i in range(N)]
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    if union[get(a - 1)] == union[get(b - 1)]:
        continue
    union[get(a - 1)] = get(b - 1)
    cnt += 1

edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append((sum(map(lambda k: (nodes[i][k] - nodes[j][k]) ** 2, range(2))), i, j))
heapify(edges)

answer = 0
for _ in range(N - cnt - 1):
    while True:
        distance, a, b = heappop(edges)
        if get(a) != get(b):
            break

    union[get(a)] = get(b)
    answer += sqrt(distance)
print(f"{answer:.2f}")