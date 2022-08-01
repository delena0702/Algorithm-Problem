from collections import deque
import sys
def input(): return sys.stdin.readline().strip()

while True:
    N = int(input())
    
    if N == 0:
        break

    nodes = [0] * (N + 1)
    edges = [[] for _ in range(N + 1)]
    edges[0] = [1]
    for here in range(1, N + 1):
        arr = input().split()

        if arr[0] == 'L':
            nodes[here] = int(arr[1])
        else:
            nodes[here] = -int(arr[1])
        
        for there in arr[2:-1]:
            edges[here].append(int(there))
    
    queue = deque([(0, 0)])
    dist = [-1] * (N + 1)
    dist[0] = 0

    while queue:
        here, cost = queue.popleft()

        if here == N:
            print("Yes")
            break

        for there in edges[here]:
            if nodes[there] >= 0:
                ncost = max(cost, nodes[there])
            else:
                ncost = cost + nodes[there]
            
            if ncost <= dist[there]:
                continue

            dist[there] = ncost
            queue.append((there, ncost))
    else:
        print("No")