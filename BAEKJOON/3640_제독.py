from collections import defaultdict, deque
import sys
def input(): return sys.stdin.readline().strip()

while True:
    try:
        V, E = map(int, input().split())
    except:
        break

    edges = [defaultdict(lambda: (-1, -1)) for _ in range(2 * V)]
    for i in range(V):
        edges[2 * i][2 * i + 1] = (1, 0)
        edges[2 * i + 1][2 * i] = (0, 0)

    for _ in range(E):
        a, b, c = map(int, input().split())
        edges[2 * a - 1][2 * b - 2] = (1, c)
        edges[2 * b - 2][2 * a - 1] = (0, -c)
    flow = [defaultdict(int) for _ in range(2 * V)]

    answer = 0
    for _ in range(2):
        dist = [float('inf')] * (2 * V)
        inqueue = [False] * (2 * V)
        pre = [-1] * (2 * V)
        dist[1], inqueue[1] = 0, True
        queue = deque([1])
        while queue:
            here = queue.popleft()
            inqueue[here] = False

            for there in edges[here].keys():
                capacity, cost = edges[here][there]

                if capacity - flow[here][there] <= 0:
                    continue

                if dist[here] + cost >= dist[there]:
                    continue

                dist[there] = dist[here] + cost
                pre[there] = here

                if not inqueue[there]:
                    queue.append(there)
                    inqueue[there] = True
        
        if pre[2 * V - 2] == -1:
            break

        there = 2 * V - 2
        while there != 1:
            here = pre[there]
            flow[here][there] = flow[here][there] + 1
            flow[there][here] = flow[there][here] - 1
            answer = answer + edges[here][there][1]
            there = here

    print(answer)