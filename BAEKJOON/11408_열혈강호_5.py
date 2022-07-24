import sys
from collections import deque
from collections import defaultdict
INF = 987654321
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
edges = [[] for _ in range(N + M + 2)]
for here in range(1, N + 1):
    (K, *temp) = map(int, input().split())
    for j in range(K):
        edges[here].append((N + temp[2*j], 1, temp[2*j+1]))
        edges[N + temp[2*j]].append((here, 0, -temp[2*j+1]))

for person in range(1, N + 1):
    edges[0].append((person, 1, 0))
    edges[person].append((0, 0, 0))

for work in range(N + 1, N + M + 1):
    edges[work].append((N + M + 1, 1, 0))
    edges[N + M + 1].append((work, 0, 0))

flow = [defaultdict(int) for _ in range(N + M + 2)]
answer = [0, 0]
while True:
    distance = [INF] * (N + M + 2)
    in_queue = [False] * (N + M + 2)
    pre = [-1] * (N + M + 2)

    in_queue[0] = True
    queue = deque([0])
    distance[0] = 0

    while queue:
        here = queue.popleft()
        in_queue[here] = False

        for (there, capacity, cost) in edges[here]:
            if capacity - flow[here][there] <= 0:
                continue
            if distance[here] + cost >= distance[there]:
                continue

            distance[there] = distance[here] + cost
            pre[there] = here

            if not in_queue[there]:
                queue.append(there)
                in_queue[there] = True

    if pre[N + M + 1] == -1:
        break

    here = N + M + 1
    while here:
        flow[pre[here]][here] += 1
        flow[here][pre[here]] -= 1

        for (there, capacity, cost) in edges[pre[here]]:
            if there == here:
                answer[1] += cost
                break

        here = pre[here]
    answer[0] += 1

print(answer[0])
print(answer[1])
