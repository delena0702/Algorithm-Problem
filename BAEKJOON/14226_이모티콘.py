from collections import defaultdict, deque

S = int(input())
dp = defaultdict(lambda: defaultdict(lambda: float('inf')))
dp[1][0] = 0
queue = deque([(1, 0)])
while queue:
    here, copied = queue.popleft()

    if here == S:
        print(dp[here][copied])
        break

    for t in [(here, here), (here + copied, copied), (here - 1, copied)]:
        if dp[t[0]][t[1]] <= dp[here][copied] + 1:
            continue

        dp[t[0]][t[1]] = dp[here][copied] + 1
        queue.append(t)