import sys
def input(): return sys.stdin.readline().strip()


dp = [[0] * 31 for _ in range(31)]


def combination(m, n):
    if n == 0 or m == n:
        return 1
    if dp[m][n]:
        return dp[m][n]
    dp[m][n] = combination(m-1, n-1) + combination(m-1, n)
    return dp[m][n]


T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    print(combination(M, N))
