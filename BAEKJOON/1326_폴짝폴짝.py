from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
data = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

queue = deque([a])
dist = [float('inf')] * (N + 1)
dist[a] = 0
while queue:
    here = queue.popleft()
    if here == b:
        print(dist[here])
        break

    for there in range((here + data[here] - 1) % data[here] + 1, N + 1, data[here]):
        if dist[there] <= dist[here] + 1:
            continue
        dist[there] = dist[here] + 1
        queue.append(there)
else:
    print(-1)