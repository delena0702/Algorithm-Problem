import sys
import heapq
INF = 987654321
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
edges = [[] for _ in range(M + N + 2)]

for i, a in enumerate(map(int, input().split())):
    edges[M + i + 1].append((M + N + 1, a, 0))
    edges[M + N + 1].append((M + i + 1, 0, 0))

for i, b in enumerate(map(int, input().split())):
    edges[0].append((i + 1, b, 0))
    edges[i + 1].append((0, 0, 0))

for i in range(1, M+1):
    for j, c in enumerate(map(int, input().split())):
        edges[i].append((M + j + 1, INF, c))
        edges[M + j + 1].append((i, 0, -c))

flow = [[0] * (M + N + 2) for _ in range(M + N + 2)]
answer = 0
while True:
    pq, distance, pre = [(0, 0, -1)], [INF] * (M + N + 2), [-1] * (M + N + 2)
    while pq:
        (d, here, parent) = heapq.heappop(pq)
        if distance[here] <= d:
            continue
        distance[here] = d
        pre[here] = parent
        if here == M + N + 1:
            pq = [1]
            break
        for (there, capacity, w) in edges[here]:
            if capacity - flow[here][there] <= 0:
                continue
            heapq.heappush(pq, (d + w, there, here))

    if not pq:
        break

    flow_min = INF
    here = M + N + 1
    while here:
        index = -1
        for i, n in enumerate(edges[pre[here]]):
            if n[0] == here:
                index = i
                break

        flow_min = min(flow_min, edges[pre[here]]
                       [index][1] - flow[pre[here]][here])
        here = pre[here]

    here = M + N + 1
    while here:
        flow[pre[here]][here] += flow_min
        flow[here][pre[here]] -= flow_min

        index = -1
        for i, n in enumerate(edges[pre[here]]):
            if n[0] == here:
                index = i
                break
        answer += flow_min*edges[pre[here]][index][2]
        here = pre[here]

print(answer)
