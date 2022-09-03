from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())

    edges = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    check = [0] * (V + 1)
    answer = False
    for i in range(1, V + 1):
        if check[i]:
            continue

        check[i] = 1
        queue = deque([i])
        while queue:
            here = queue.popleft()

            for there in edges[here]:
                if check[there] == check[here]:
                    answer = True
                    break

                if check[there]:
                    continue

                check[there] = 3 - check[here]
                queue.append(there)
            
            if answer:
                break
            
        if answer:
            break
    
    print("NO" if answer else "YES")