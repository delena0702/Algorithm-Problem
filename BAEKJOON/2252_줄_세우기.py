from collections import defaultdict
from graphlib import TopologicalSorter
import sys
def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())

graph = defaultdict(set)
for i in range(1, N + 1):
    graph[i]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].add(a)

print(*TopologicalSorter(graph).static_order())