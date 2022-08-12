import sys
def input(): return sys.stdin.readline().strip()

SIZE_N, SIZE_K = 1120, 14

is_prime = [True] * (SIZE_N + 1)
primes = []
for i in range(2, SIZE_N + 1):
    if not is_prime[i]:
        continue
    for j in range(2 * i, SIZE_N + 1, i):
        is_prime[j] = False
    primes.append(i)

dp = [[0] * (SIZE_K + 1) for _ in range(SIZE_N + 1)]
dp[0][0] = 1
for prime in primes:
    for i in range(SIZE_N, prime - 1, -1):
        for j in range(1, SIZE_K + 1):
            dp[i][j] = dp[i][j] + dp[i - prime][j - 1]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(dp[n][k])