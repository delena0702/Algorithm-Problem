import sys
def input(): return sys.stdin.readline().strip()


(N, K) = map(int, input().split())
data, dp = [], [[-1] * (K + 1) for _ in range(N)]
for i in range(N):
    data.append(tuple(map(int, input().split())))
data.sort(key=lambda x: (-x[0], -x[1]))


def solve(index, weight):
    if index == N or weight == 0:
        return 0
    if dp[index][weight] != -1:
        return dp[index][weight]

    dp[index][weight] = solve(index + 1, weight)

    if weight >= data[index][0]:
        dp[index][weight] = max(dp[index][weight], solve(
            index + 1, weight - data[index][0]) + data[index][1])

    return dp[index][weight]


print(solve(0, K))
