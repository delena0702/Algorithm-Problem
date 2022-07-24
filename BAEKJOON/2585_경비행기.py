import sys
from collections import deque
from math import ceil, sqrt
def input(): return sys.stdin.readline().strip()


N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
data = [[0, 0], [10000, 10000], *data]


def canReach(volume):
    visited = [False for _ in range(N + 2)]
    queue = deque([(0, 0)])

    while(queue):
        here, count = queue.popleft()

        if here == 1:
            return True

        for there in range(1, N + 2):
            if ceil(sqrt((data[here][0] - data[there][0]) ** 2 +
                         (data[here][1] - data[there][1]) ** 2) / 10) > volume:
                continue

            if visited[there]:
                continue

            if (count + 1 > K + 1):
                continue

            visited[there] = True
            queue.append((there, count + 1))

    return False


lo, hi = 0, 20000
while lo < hi:
    mi = (lo + hi) // 2
    if canReach(mi):
        hi = mi
    else:
        lo = mi + 1
print(lo)
