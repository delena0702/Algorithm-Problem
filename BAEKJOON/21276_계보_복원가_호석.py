from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = input().split()
M = int(input())
edges = [input().split() for _ in range(M)]

counts = defaultdict(int)
for child, parent in edges:
    counts[parent] = counts[parent] + 1

parents = {}
for child, parent in edges:
    if child not in parents or counts[parent] < counts[parents[child]]:
        parents[child] = parent

children = defaultdict(list)
for name in data:
    children[name]
    
for child, parent in parents.items():
    children[parent].append(child)

roots = list(sorted(set(data).difference(set(map(lambda x: x[0], edges)))))
print(len(roots))
print(*roots, sep=' ')

for parent, arr in sorted(children.items()):
    print(parent, len(arr), *sorted(arr), sep=' ')