from math import isinf
import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()

def parse(ch):
    if ch >= 'a' and ch <= 'z':
        return ord(ch) - ord('a') + 1
    if ch >= 'A' and ch <= 'Z':
        return ord(ch) - ord('A') + 27
    return float('inf')

N = int(input())
data = [list(map(parse, input())) for _ in range(N)]
answer = sum(filter(lambda x: not isinf(x), sum(data, [])))
queue, visited = [(0, 0, -1)], [False] * N

while queue:
    (distance, here, pre_node) = heappop(queue)

    if visited[here]:
        continue

    visited[here] = True

    if pre_node != -1:
        answer = answer - min(data[here][pre_node], data[pre_node][here])

    for there in range(N):
        if visited[there]:
            continue

        d = min(data[here][there], data[there][here])
        if isinf(d):
            continue

        heappush(queue, (d, there, here))

if visited.count(False):
    print(-1)
else:
    print(answer)