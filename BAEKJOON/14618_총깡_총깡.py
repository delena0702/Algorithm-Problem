import sys
import heapq

def input(): return sys.stdin.readline().strip()

N, M = map(int, input().split())
J = int(input())
K = int(input())
a_node = list(map(int, input().split()))
b_node = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for i in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

dijkstra = [-1 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
queue = [(0, J)]
answer = ['', -1]

while queue:
    (distance, here) = heapq.heappop(queue)

    if visited[here]: continue

    if answer[1] != -1 and distance > answer[1]:
        break

    if here in a_node:
        answer[0] = 'A'
        answer[1] = distance
        break

    if here in b_node:
        answer[0] = 'B'
        answer[1] = distance

    visited[here] = True
    dijkstra[here] = distance

    for (there, weight) in graph[here]:
        if (visited[there]): continue
        heapq.heappush(queue, (distance + weight, there))
        pass
    pass

if (answer[1] == -1):
    print("-1")
else:
    print(*answer, sep='\n')