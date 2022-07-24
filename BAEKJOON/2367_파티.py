import sys
(N, K, D) = map(int, sys.stdin.readline().strip().split())

# 탐색을 위한 엣지 정보 저장
edges = [[] for i in range(N+D+2)]
flow = {}
for i in range(1, N+1):
    edges[0].append((i, K))
    edges[i].append((0, 0))

for (i, food_limit) in enumerate(map(int, sys.stdin.readline().strip().split())):
    edges[N+i+1].append((N+D+1, food_limit))
    edges[N+D+1].append((N+i+1, 0))

for i in range(1, N+1):
    for food in list(map(int, sys.stdin.readline().strip().split()))[1:]:
        edges[i].append((N+food, 1))
        edges[N+food].append((i, 0))

answer = 0
while True:
    # 경로를 BFS로 탐색
    q = [0]
    visited = [-1]*(N+D+2)
    while q:
        if q[0] == N+D+1:
            break
        here = q.pop(0)
        for (there, weight) in edges[here]:
            if visited[there] != -1: continue
            if weight - flow.get((here, there), 0) <= 0 : continue
            visited[there] = here
            q.append(there)
    if not q:
        break

    # flow 흘려보내줌
    here = N+D+1
    while here != 0:
        flow[(visited[here], here)] = flow.get((visited[here], here), 0) + 1
        flow[(here, visited[here])] = flow.get((here, visited[here]), 0) - 1
        here = visited[here]
    answer += 1

print(answer)
