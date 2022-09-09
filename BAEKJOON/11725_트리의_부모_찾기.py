from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

answer = [0] * (N + 1)
queue = deque([1])
answer[1] = -1

while queue:
    here = queue.popleft()

    for there in edges[here]:
        if answer[there]:
            continue

        answer[there] = here
        queue.append(there)

print(*answer[2:], sep='\n')