import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


(N, M) = map(int, input().split())
arr = [0]*N
for i in range(N):
    arr[i] = list(map(int, input().split()))

answer = 0
direct = ((0, 1), (0, -1), (1, 0), (-1, 0))
while True:
    queue = deque([0])
    cheese_check = [False]*(N*M)
    visited = [False]*(N*M)
    check = True

    while (queue):
        here = queue.popleft()
        (y, x) = divmod(here, M)

        if arr[y][x]:
            cheese_check[here] = True
            check = False
            continue

        if visited[here]:
            continue
        visited[here] = True

        for (dx, dy) in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            queue.append(M*ny+nx)

    if check:
        break

    for (here, value) in enumerate(cheese_check):
        if not value:
            continue
        (y, x) = divmod(here, M)
        cnt = 0
        for (dx, dy) in direct:
            if visited[M*(y+dy)+(x+dx)]:
                cnt += 1
        if cnt >= 2:
            arr[y][x] = 0

    answer += 1

print(answer)
