import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    data = [0] + list(map(int, input().split()))

    psum = [0] * (N + 1)
    for i in range(1, N + 1):
        psum[i] = psum[i - 1] + data[i]

    idx = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        idx[i][i] = i

    dp = [[0] * (N + 1) for _ in range(N + 1)]    
    for i in range(1, N):
        for j in range(1, N - i + 1):
            s, e = j, j + i

            k = idx[s][e - 1]
            idx[s][e] = k
            dp[s][e] = dp[s][k] + dp[k + 1][e]
            for k in range(k + 1, idx[s + 1][e] + 1):
                if dp[s][e] > dp[s][k] + dp[k + 1][e]:
                    idx[s][e] = k
                    dp[s][e] = dp[s][k] + dp[k + 1][e]

            dp[s][e] += psum[e] - psum[s - 1]
    
    print(dp[1][N])
