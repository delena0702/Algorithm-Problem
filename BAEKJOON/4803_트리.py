from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


test_case = 1
while True:
    N, M = map(int, input().split())
    if N == 0:
        break

    edges = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    answer = 0
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True

        is_tree = True
        queue = deque([(i, 0)])
        while queue:
            here, pre = queue.popleft()
            for there in edges[here]:
                if there == pre:
                    continue

                if visited[there]:
                    is_tree = False
                    continue
                visited[there] = True

                queue.append((there, here))

        if is_tree:
            answer = answer + 1

    print(f"Case {test_case}: ", end='')
    if answer == 0:
        print("No trees.")
    elif answer == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {answer} trees.")
    test_case = test_case + 1
