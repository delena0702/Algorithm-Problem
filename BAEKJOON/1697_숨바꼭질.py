from collections import deque

N, K = map(int, input().split())
if N >= K:
    print(N - K)
    exit()

queue = deque([(N, 0)])
dp = set([N])
while queue:
    here, depth = queue.popleft()

    if here == K:
        print(depth)
        break

    for there in [here * 2, here + 1, here - 1]:
        if there in dp:
            continue
        if there > 2 * K:
            continue
        dp.add(there)
        queue.append((there, depth + 1))